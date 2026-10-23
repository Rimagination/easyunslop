#!/usr/bin/env python3
"""Read-only lexical editing candidates, with an optional comparable reference corpus.

Adapted from the parent project's standard-library excess_vocab.py. English words
and two/three-word phrases, or Chinese two/three-character groups, describe usage;
they do not estimate AI authorship. Newlines and sentence punctuation delimit
phrases conservatively. Chinese character groups are not word segmentation.
"""

import argparse
from bisect import bisect_right
from collections import Counter
import html
import json
import os
from pathlib import Path
import re
import sys
import tempfile


HAN = re.compile(r"[\u4e00-\u9fff]+")
EN_TOKEN = re.compile(r"[A-Za-z][A-Za-z'’\-]*")
BOUNDARY = re.compile(r"[.!?。！？;；:\n\r\x00\u4e00-\u9fff]+")
SOFT = "\x01"
INLINE_TAGS = {"a", "abbr", "b", "bdi", "bdo", "cite", "del", "em", "i", "ins",
               "mark", "q", "s", "small", "span", "strong", "sub", "sup", "u"}
DEFAULT_LEXICON = Path(__file__).resolve().parents[1] / "references" / "lexical-signals.json"
EN_STOP = set(
    """a an the and or but for nor so yet of to in on at by as is it be are was were
    been being this that these those from with into than also both each such more most
    other some only over under between within without after before during while where
    when what our its they them then there here all any not per via one two three used
    using use may can could would should did does do had has have how who whom whose
    however although whereas because therefore thus hence about above across against
    along among around given though until upon we us you your he she his her their
    i me my if no up out off own same too very just""".split()
)


def _mask(text, marker="\x00"):
    """Keep line offsets and prevent phrases from bridging removed material."""
    return re.sub(r"[^\n]", marker, text)


def _sub_mask(pattern, text, flags=0, marker="\x00"):
    return re.sub(pattern, lambda match: _mask(match.group(), marker), text, flags=flags)


def _unwrap_formatting(text):
    """Keep wrapper offsets while letting natural-language tokens join through them."""
    for pattern in (r"(?<![\\*])(\*{1,3})(?!\*)(?=\S)([^\n\x00]*?\S)\1(?!\*)",
                    r"(?<![\\\w])(_{1,3})(?!_)(?=\S)([^\n\x00]*?\S)\1(?![\w_])"):
        while True:
            unwrapped = re.sub(pattern, lambda match: _mask(match[1], SOFT) + match[2] + _mask(match[1], SOFT), text)
            if unwrapped == text:
                break
            text = unwrapped
    characters = list(text)
    for match in re.finditer(r"\\(?:emph|textit|textbf|textnormal|textrm|textsf|texttt|textsc|underline)\*?\s*\{", text):
        depth = 1
        for index in range(match.end(), len(text)):
            if text[index] in "{}" and text[index - 1] != "\\":
                depth += 1 if text[index] == "{" else -1
                if depth == 0:
                    characters[match.start():match.end()] = _mask(match.group(), SOFT)
                    characters[index] = SOFT
                    break
    return "".join(characters)


def _heading(line):
    markdown = re.match(r"^\s{0,3}(#{1,6})\s+(.+?)\s*#*\s*$", line)
    latex = re.match(r"^\s*\\(section|subsection|subsubsection)\*?\{([^{}]+)\}\s*$", line)
    if markdown:
        return len(markdown[1]), markdown[2]
    if latex:
        return {"section": 1, "subsection": 2, "subsubsection": 3}[latex[1]], latex[2]
    return None, line.strip()


def clean_text(text):
    """Remove markup/code/citation keys/math while retaining natural language."""
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = _sub_mask(r"<!--(?:.*?-->|.*\Z)", text, re.S)
    text = _sub_mask(r"<(script|style|pre|code)\b[^>]*>.*?</\1\s*>", text, re.I | re.S)
    lines, fence, fence_length = [], None, 0
    for line in text.splitlines(keepends=True):
        marker = re.match(r"^\s{0,3}(`{3,}|~{3,})(.*)$", line)
        if fence:
            lines.append(_mask(line))
            if marker and marker[1][0] == fence and len(marker[1]) >= fence_length and not marker[2].strip():
                fence = None
        elif marker:
            fence, fence_length = marker[1][0], len(marker[1])
            lines.append(_mask(line))
        else:
            lines.append(line)
    text = "".join(lines)
    text = _sub_mask(r"(?<!`)(`+)(?!`)(.*?)\1(?!`)", text, re.S)

    # Isolate generated references, leaving the next normal section untouched.
    text = _sub_mask(r"\\begin\s*\{thebibliography\}.*?\\end\s*\{thebibliography\}", text, re.S)
    text = _sub_mask(r"\\datalist\b.*?\\enddatalist\b|\\entry\s*\{.*?\\endentry\b", text, re.S)
    text = _sub_mask(r"\\(?:printbibliography|printbiblist)\b(?:\s*\[[^\]]*\])*(?:\s*\{[^{}]*\})?", text)
    text = _sub_mask(r"\\refsection\s*\{[^{}]*\}|\\endrefsection\b", text)

    lines, reference_level = [], None
    reference_title = re.compile(r"^(?:\d+(?:\.\d+)*[.)、]?\s*)?(?:references|bibliography|参考文献)\s*[:：]?\s*$", re.I)
    for line in text.splitlines(keepends=True):
        level, title = _heading(line)
        # Plain and setext reference headings conventionally run to the end.
        if reference_title.fullmatch(title.strip().strip("*_")):
            reference_level = level or 0
        elif reference_level is not None and reference_level > 0 and level is not None and level <= reference_level:
            reference_level = None
        lines.append(_mask(line) if reference_level is not None else line)
    text = "".join(lines)

    text = _sub_mask(r"\\begin\{(equation\*?|align\*?|alignat\*?|gather\*?|multline\*?|displaymath|math)\}.*?\\end\{\1\}", text, re.S)
    text = _sub_mask(r"\\\[.*?\\\]|\\\(.*?\\\)", text, re.S)
    text = _sub_mask(r"(?<!\\)\$\$.*?(?<!\\)\$\$", text, re.S)
    text = _sub_mask(r"(?<![\\$])\$(?!\$)(?:\\.|[^$])*?(?<!\\)\$", text, re.S)
    cite_args = r"(?:\s*\[[^\]]*\])*\s*\{[^{}]*\}"
    # Only explicit multicite commands consume repeated mandatory arguments.
    text = _sub_mask(r"\\(?:[Cc]ites|(?:auto|paren|text|foot|smart|super|full|footfull|note)[Cc]ites)\*?(?:" + cite_args + r")+", text)
    text = _sub_mask(r"\\(?:[Cc]ite[A-Za-z]*|(?:auto|paren|text|foot|smart|super|full|footfull|note)[Cc]ite[A-Za-z]*|nocite)\*?" + cite_args, text)
    text = _sub_mask(r"\\(?:[Ee]qref|[Aa]utoref|[Cc]ref|[Vv]ref|ref|pageref|label|bibitem|bibliography|addbibresource|bibliographystyle)\*?(?:\s*\[[^\]]*\])*\s*\{[^{}]*\}", text)
    text = _sub_mask(r"\[[^\]\n]*@[A-Za-z0-9][^\]\n]*\]", text)
    text = _sub_mask(r"(?<!\w)@[A-Za-z0-9][\w:.+\-/]*", text)
    text = _sub_mask(r"^\s{0,3}\[[^\]\n]+\]:[^\n]*", text, re.M)
    # Keep the readable label in [label](URL) and images/captions.
    text = _sub_mask(r"\]\(\s*(?:<[^>\n]*>|(?:\\.|[^)\n])*)\)", text)
    text = re.sub(r'''</?([A-Za-z][A-Za-z0-9:-]*)(?:\s+[A-Za-z_:][A-Za-z0-9_.:-]*(?:\s*=\s*(?:"[^"]*"|'[^']*'|[^\s"'=<>`]+))?)*\s*/?>''',
                  lambda match: _mask(match.group(), SOFT if match[1].lower() in INLINE_TAGS else "\x00"), text)
    text = _sub_mask(r"(?:https?://|www\.)[^\s<>\x00]+", text, re.I)
    text = _unwrap_formatting(text)
    # Other commands, headings, and captions retain their braced prose.
    text = _sub_mask(r"\\[A-Za-z]+\*?", text)
    return text


def read_text(path):
    return clean_text(Path(path).read_text(encoding="utf-8-sig"))


def iter_ref_files(ref_dir):
    for root, directories, files in os.walk(ref_dir):
        directories.sort()
        for name in sorted(files):
            if not name.lower().startswith("readme") and name.lower().endswith((".md", ".txt")):
                yield Path(root) / name


def detect_lang(text):
    han = sum(len(run) for run in HAN.findall(text))
    latin = len(re.findall(r"[A-Za-z]", text))
    return "zh" if han and han / (han + latin) > 0.3 else "en"


def available_languages(text):
    return [lang for lang, pattern in (("zh", HAN), ("en", EN_TOKEN)) if pattern.search(text)]


def zh_ngrams(text):
    return [run[index:index + size] for run in HAN.findall(text.replace(SOFT, ""))
            for size in (2, 3) for index in range(len(run) - size + 1)]


def en_words(text):
    return [word.lower() for word in EN_TOKEN.findall(text.replace(SOFT, ""))
            if len(word) >= 3 and word.lower() not in EN_STOP]


def en_phrases(text):
    out = []
    for sentence in BOUNDARY.split(text.replace(SOFT, "")):
        tokens = [word.lower() for word in EN_TOKEN.findall(sentence)]
        for size in (2, 3):
            for index in range(len(tokens) - size + 1):
                gram = tokens[index:index + size]
                if not all(token in EN_STOP or len(token) < 3 for token in gram):
                    out.append(" ".join(gram))
    return out


def excess_tables(target_counts, ref_counts, top, min_count):
    """Use observed rates, without smoothing or invented absent-word ratios."""
    n_target, n_ref = sum(target_counts.values()), sum(ref_counts.values())
    repeated, seen, unseen = [], [], []
    for token, count in target_counts.items():
        if count < min_count:
            continue
        ref_count = ref_counts.get(token, 0)
        target_rate = count / n_target * 1000
        ref_rate = ref_count / n_ref * 1000 if n_ref else None
        row = {"token": token, "target": count, "ref": ref_count if n_ref else None,
               "target_per_1000": round(target_rate, 3),
               "ref_per_1000": round(ref_rate, 3) if ref_rate is not None else None,
               "ratio": round(target_rate / ref_rate, 3) if ref_rate else None}
        repeated.append(row)
        if n_ref:
            (seen if ref_count else unseen).append(row)
    repeated.sort(key=lambda row: (-row["target"], row["token"]))
    seen.sort(key=lambda row: (-row["ratio"], -row["target"], row["token"]))
    unseen.sort(key=lambda row: (-row["target"], row["token"]))
    return {"repeated": repeated[:top], "seen": seen[:top], "unseen": unseen[:top],
            "n_target": n_target, "n_ref": n_ref, "baseline": bool(n_ref),
            "repeated_total": len(repeated)}


def load_lexicon(path, profile):
    data = json.loads(Path(path).read_text(encoding="utf-8-sig"))
    if not isinstance(data, dict) or type(data.get("version")) is not int or data["version"] != 1:
        raise ValueError("词库 version 必须为 1")
    sources, entries = data.get("sources"), data.get("entries")
    if not isinstance(sources, dict) or not isinstance(entries, list):
        raise ValueError("词库需要 sources 对象与 entries 数组")
    for source_id, source in sources.items():
        if not isinstance(source_id, str) or not source_id.strip() or not isinstance(source, dict):
            raise ValueError("词库来源 ID 和对象无效")
        if any(not isinstance(source.get(key), str) or not source[key].strip() for key in ("title", "url", "evidence")):
            raise ValueError(f"词库来源 {source_id} 需要 title、url、evidence 字符串")
    known_profiles, ids = {"general"}, set()
    for entry in entries:
        if not isinstance(entry, dict) or not isinstance(entry.get("id"), str) or not entry["id"].strip():
            raise ValueError("词库条目缺少有效 id")
        entry_id = entry["id"]
        if entry_id in ids:
            raise ValueError(f"词库条目 ID 重复：{entry_id}")
        ids.add(entry_id)
        if entry.get("lang") not in ("en", "zh"):
            raise ValueError(f"词库条目 {entry_id} 的 lang 必须为 en 或 zh")
        for key in ("forms", "profiles", "sources"):
            values = entry.get(key)
            if not isinstance(values, list) or not values or any(not isinstance(value, str) or not value.strip() for value in values):
                raise ValueError(f"词库条目 {entry_id} 的 {key} 需要非空字符串数组")
        forms = [form.casefold().strip() if entry["lang"] == "en" else form.strip() for form in entry["forms"]]
        if len(set(forms)) != len(forms):
            raise ValueError(f"词库条目 {entry_id} 的 forms 重复")
        if any(source not in sources for source in entry["sources"]):
            raise ValueError(f"词库条目 {entry_id} 引用了不存在的来源")
        if any(not isinstance(entry.get(key), str) or not entry[key].strip() for key in ("review", "preserve")):
            raise ValueError(f"词库条目 {entry_id} 需要 review、preserve 字符串")
        known_profiles.update(entry["profiles"])
    if profile not in known_profiles:
        raise ValueError(f"未知 profile：{profile}；可用：{', '.join(sorted(known_profiles))}")
    return data


def lexical_candidates(documents, lexicon, lang, profile, top):
    """Count every eligible entry before ranking; keep up to five hit contexts."""
    candidates = []
    languages = {lang} if isinstance(lang, str) else set(lang)
    prepared = []
    for path, text in documents:
        offsets = [index for index, character in enumerate(text) if character != SOFT] if SOFT in text else None
        prepared.append((path, text, text.replace(SOFT, ""), offsets,
                         [0] + [match.end() for match in re.finditer("\n", text)]))
    for entry in lexicon["entries"]:
        if entry["lang"] not in languages or not ({"general", profile} & set(entry["profiles"])):
            continue
        forms = [re.escape(form.strip()) for form in sorted(entry["forms"], key=len, reverse=True)]
        pattern = "(?:" + "|".join(forms) + ")"
        if entry["lang"] == "en":
            pattern = r"(?<![A-Za-z0-9_'’\-])" + pattern.replace(r"\ ", r"[ \t]+") + r"(?![A-Za-z0-9_'’\-])"
        matcher = re.compile(pattern, re.I if entry["lang"] == "en" else 0)
        count, occurrences = 0, []
        for path, text, view, offsets, starts in prepared:
            for match in matcher.finditer(view):
                count += 1
                if len(occurrences) < 5:
                    start = offsets[match.start()] if offsets is not None else match.start()
                    end = offsets[match.end() - 1] + 1 if offsets is not None else match.end()
                    line_number = bisect_right(starts, start)
                    line_start = starts[line_number - 1]
                    line_end = text.find("\n", end)
                    line_end = len(text) if line_end < 0 else line_end
                    context_start = max(line_start, start - 65)
                    context_end = min(line_end, end + 65)
                    context = re.sub(r"[\s\x00]+", " ", text[context_start:context_end].replace(SOFT, "")).strip()
                    occurrences.append({"file": str(path), "line": line_number,
                                        "match": match.group(), "context": context})
        if count:
            candidates.append({"id": entry["id"], "forms": entry["forms"], "count": count,
                               "occurrences": occurrences, "review": entry["review"],
                               "preserve": entry["preserve"], "sources": entry["sources"]})
    candidates.sort(key=lambda entry: (-entry["count"], entry["id"]))
    return candidates[:top], len(candidates)


def _md(value):
    return html.escape(str(value), quote=False).replace("|", "\\|").replace("\n", " ")


def render_report(result):
    lines = [f"# 词汇编辑候选（{' / '.join(result['scan_languages'])}）", "",
             "- 高频、重复和参照差异均供人工编辑复核；不计算 AI 概率。领域术语、缩写及必要表达应结合语境保留。",
             "- 中文统计为汉字二三元字组，并非中文分词；英文词组在句子标点、换行、中文片段和块级标签处断开。",
             f"- 扫描语言：{'、'.join(result['scan_languages'])}；各语言分别统计，混合参照仅贡献相应语言的统计单位。",
             f"- 目标：{', '.join(_md(path) for path in result['targets'])}",
             f"- 词库 profile：{_md(result['profile'])}；同时检查 general 条目。",
             f"- 有效参照文件：{len(result['reference_files'])}；未提供有效参照时只报告稿内重复和词库候选。", ""]
    for warning in result["warnings"]:
        lines.append(f"提示：{_md(warning)}")
    lines += ["", "## 词库编辑候选", "",
              f"完整扫描命中 {result['lexical_candidates_total']} 个条目，显示前 {len(result['lexical_candidates'])} 个；一次命中也列入候选。", ""]
    for candidate in result["lexical_candidates"]:
        lines += [f"### {_md(candidate['id'])}：{candidate['count']} 次", "",
                  f"形式：{_md(', '.join(candidate['forms']))}", "",
                  f"复核：{_md(candidate['review'])}", "", f"保留：{_md(candidate['preserve'])}", ""]
        for occurrence in candidate["occurrences"]:
            lines.append(f"- {_md(occurrence['file'])}，行 {occurrence['line']}：{_md(occurrence['context'])}")
        if candidate["count"] > len(candidate["occurrences"]):
            lines.append(f"- 上文展示前 {len(candidate['occurrences'])} 处，共 {candidate['count']} 次。")
        lines += ["", "来源 ID：" + ", ".join(_md(source) for source in candidate["sources"]), ""]
    used_sources = {source for candidate in result["lexical_candidates"] for source in candidate["sources"]}
    for source_id in sorted(used_sources):
        source = result["lexicon"]["sources"][source_id]
        lines.append(f"- {_md(source_id)}：{_md(source['title'])}；{_md(source['url'])}；{_md(source['evidence'])}")
    for title, table in result["blocks"].items():
        lines += ["", f"## {title}", "", f"目标统计单位 {table['n_target']}；参照统计单位 {table['n_ref']}（{len(table['reference_files'])} 个有效参照文件）。", "",
                  "### 稿内重复", "", "| 词/字组 | 目标次数 | 每千统计单位 |", "|---|---:|---:|"]
        lines += [f"| {_md(row['token'])} | {row['target']} | {row['target_per_1000']} |" for row in table["repeated"]]
        if table["baseline"]:
            lines += ["", "### 参照中也出现的候选", "", "| 词/字组 | 目标次数 | 参照次数 | 目标/千 | 参照/千 | 相对频次比 |", "|---|---:|---:|---:|---:|---:|"]
            lines += [f"| {_md(row['token'])} | {row['target']} | {row['ref']} | {row['target_per_1000']} | {row['ref_per_1000']} | {row['ratio']} |" for row in table["seen"]]
            lines += ["", "### 参照中未出现的候选", "", "| 词/字组 | 目标次数 |", "|---|---:|"]
            lines += [f"| {_md(row['token'])} | {row['target']} |" for row in table["unseen"]]
            lines += ["", "相对频次比依据两组各自统计单位归一化；参照零命中时不计算倍数。"]
    return "\n".join(lines) + "\n"


def _same_path(first, second):
    return (os.path.normcase(str(first.resolve())) == os.path.normcase(str(second.resolve()))
            or (first.exists() and second.exists() and os.path.samefile(first, second)))


def validate_outputs(outputs, inputs):
    for index, output in enumerate(outputs):
        for source in inputs + outputs[:index]:
            if _same_path(output, source):
                raise ValueError(f"输出不能覆盖目标、参照、词库或另一个输出：{output}")
        if not output.parent.is_dir() or output.is_dir():
            raise ValueError(f"输出需要现有目录中的文件路径：{output}")


def _write_atomic(path, content):
    temporary = None
    try:
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False) as handle:
            temporary = Path(handle.name)
            handle.write(content)
        os.replace(temporary, path)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()


def main(argv=None):
    parser = argparse.ArgumentParser(description="只读词汇诊断：稿内重复、词库编辑候选及可选参照频次")
    parser.add_argument("--target", required=True, nargs="+", help="一个或多个 UTF-8 目标文本")
    parser.add_argument("--ref", help="可选参照目录：递归读取 md/txt，跳过 README")
    parser.add_argument("--lang", choices=("auto", "zh", "en"), default="auto")
    parser.add_argument("--top", type=int, default=40)
    parser.add_argument("--min-count", type=int, default=3, help="重复统计最低次数；词库候选不受此项限制")
    parser.add_argument("--profile", default="general")
    parser.add_argument("--lexicon", type=Path, default=DEFAULT_LEXICON)
    parser.add_argument("--out", type=Path, help="Markdown 输出路径；默认打印")
    parser.add_argument("--json", type=Path, help="JSON 输出路径")
    args = parser.parse_args(argv)
    try:
        if args.top < 1 or args.min_count < 1:
            raise ValueError("--top 和 --min-count 必须为正整数")
        targets = list(dict.fromkeys(Path(path).resolve() for path in args.target))
        for path in targets:
            if not path.is_file():
                raise ValueError(f"目标文件不存在：{path}")
        ref_files = []
        if args.ref:
            ref_dir = Path(args.ref).resolve()
            if not ref_dir.is_dir():
                raise ValueError(f"参照目录不存在：{ref_dir}")
            ref_files = list(iter_ref_files(ref_dir))
        outputs = [path.resolve() for path in (args.out, args.json) if path is not None]
        validate_outputs(outputs, targets + ref_files + [args.lexicon.resolve()])
        try:
            lexicon = load_lexicon(args.lexicon, args.profile)
        except (OSError, UnicodeError, ValueError) as error:
            raise ValueError(f"词库无效 {args.lexicon}：{error}") from error
        documents = [(path, read_text(path)) for path in targets]
        for path, text in documents:
            if not re.search(r"[A-Za-z\u4e00-\u9fff]", text):
                raise ValueError(f"目标为空或清洗后没有可扫描正文：{path}")
        combined_text = "\n".join(text for _, text in documents)
        lang = detect_lang(combined_text) if args.lang == "auto" else args.lang
        scan_languages = available_languages(combined_text) if args.lang == "auto" else [args.lang]
        warnings, references = [], []
        for path in ref_files:
            if any(_same_path(path, target) for target in targets):
                warnings.append(f"参照跳过目标本身：{path}")
                continue
            try:
                text = read_text(path)
            except (OSError, UnicodeError) as error:
                warnings.append(f"参照无法读取，已跳过 {path}：{error}")
                continue
            if not re.search(r"[A-Za-z\u4e00-\u9fff]", text):
                warnings.append(f"参照为空或清洗后无正文，已跳过：{path}")
            elif not set(available_languages(text)) & set(scan_languages):
                warnings.append(f"参照语言不匹配，已跳过 {path}：检测含 {'/'.join(available_languages(text))}，扫描 {'/'.join(scan_languages)}")
            else:
                references.append((path, text))
        if args.ref and not references:
            warnings.append("没有有效且语言匹配的 md/txt 参照；仅报告稿内重复和词库候选，不建立参照基线。")
        counters = {}
        if "zh" in scan_languages:
            counters["汉字二三元字组（并非分词）"] = ("zh", zh_ngrams)
        if "en" in scan_languages:
            counters.update({"英文单词": ("en", en_words), "英文二三元词组": ("en", en_phrases)})
        blocks = {}
        for title, (block_lang, tokenize) in counters.items():
            target_counts, ref_counts = Counter(), Counter()
            block_references = []
            for _, text in documents:
                target_counts.update(tokenize(text))
            for path, text in references:
                counts = Counter(tokenize(text))
                if counts:
                    ref_counts.update(counts)
                    block_references.append(str(path))
            blocks[title] = excess_tables(target_counts, ref_counts, args.top, args.min_count)
            blocks[title].update({"lang": block_lang, "reference_files": block_references})
            if args.ref and not ref_counts:
                warnings.append(f"{title}没有可用参照统计单位，仅报告该类稿内重复，不建立该类基线。")
            elif ref_counts and blocks[title]["n_ref"] < 100:
                warnings.append(f"{title}参照仅 {blocks[title]['n_ref']} 个统计单位；小样本的频次比受个别用词影响，需结合上下文复核。")
        candidates, candidate_total = lexical_candidates(documents, lexicon, scan_languages, args.profile, args.top)
        result = {"lang": lang, "scan_languages": scan_languages,
                  "targets": [str(path) for path in targets], "profile": args.profile,
                  "ref": str(Path(args.ref).resolve()) if args.ref else None,
                  "reference_files": [str(path) for path, _ in references], "warnings": warnings,
                  "lexicon": {"path": str(args.lexicon.resolve()), "version": lexicon["version"], "sources": lexicon["sources"]},
                  "lexical_candidates": candidates, "lexical_candidates_total": candidate_total, "blocks": blocks}
        report = render_report(result)
        if args.json:
            _write_atomic(args.json.resolve(), json.dumps(result, ensure_ascii=False, indent=2) + "\n")
        if args.out:
            _write_atomic(args.out.resolve(), report)
            print(f"已写入 {args.out}")
        else:
            if hasattr(sys.stdout, "reconfigure"):
                sys.stdout.reconfigure(encoding="utf-8")
            print(report, end="")
        for warning in warnings:
            print(f"提示：{warning}", file=sys.stderr)
        return 0
    except (OSError, UnicodeError, ValueError) as error:
        print(f"错误：{error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
