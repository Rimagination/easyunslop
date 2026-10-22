#!/usr/bin/env python3
"""Run with Python; standard-library assertions use only disposable fixtures."""

from collections import Counter
from contextlib import redirect_stderr, redirect_stdout
import io
import json
from pathlib import Path
import tempfile

import excess_vocab as scan


def main():
    def entry(entry_id, form, profile="general", lang="en"):
        return {"id": entry_id, "lang": lang, "forms": [form], "profiles": [profile],
                "sources": ["fixture"], "review": "Review the sentence in context.",
                "preserve": "Keep precise domain terminology and necessary descriptions."}

    lexicon = {"version": 1, "sources": {"fixture": {"title": "Self-authored fixture",
               "url": "https://example.invalid/fixture", "evidence": "Test data, no empirical claim."}},
               "entries": [entry("delve", "delve"), entry("single", "illustrates"),
                           entry("carbon", "carbon turnover"), entry("excluded", "artifactnoise"),
                           entry("ecology", "resilience", "ecology"),
                           entry("medical", "seasonal", "medical"), entry("zh", "深入", lang="zh")]}
    manuscript = r'''# Delve into canopy
Figure 1. Carbon turnover illustrates seasonal change.
\caption{Canopy resilience}
Delve into carbon turnover. Delved into sediment records.
Carbon turnover persists. Carbon turnover persists.
`inlinecodenoise artifactnoise`
```python
artifactnoise = "fencedcodenoise"
```
~~~text
artifactnoise fencedtildenoise
~~~
<!-- artifactnoise commentnoise -->
\citep[see]{citationnoise2024} \ref{referencekeynoise} \label{labelkeynoise}
[@pandocnoise2024; @pandocsecondnoise] @barecitationnoise
\(formulanoise\) $dollarnoisemath$ $$displaynoisemath$$
\begin{align} environmentnoisemath \end{align}
<span class="htmltagnoise">Visible caption</span>
[linked natural prose](https://urlnoise.example/slugnoise)
## References
referencenoise artifactnoise Delve into carbon turnover.
## Appendix
Appendix prose.
'''
    cleaned = scan.clean_text(manuscript)
    words = set(scan.en_words(cleaned))
    assert not any("noise" in word for word in words), words
    assert {"canopy", "resilience", "caption", "visible", "linked", "natural", "appendix"} <= words
    assert len(cleaned.splitlines()) == len(manuscript.splitlines()), "Line numbers must survive cleaning"
    comparison = scan.clean_text('below < 0.1 threshold and above > 0.5 <span title="x > y">control</span>')
    assert all(word in comparison for word in ("below", "threshold", "above", "control"))
    phrases = scan.en_phrases("alpha. beta!\ngamma delta\n\nepsilon zeta")
    assert "gamma delta" in phrases and "epsilon zeta" in phrases
    assert not {"alpha beta", "beta gamma", "delta epsilon"} & set(phrases)
    assert scan.en_phrases(scan.clean_text("alpha `hidden` beta")) == [], "Removed code must not join phrases"
    assert scan.en_phrases("alpha") + scan.en_phrases("beta") == [], "Files must tokenize independently"
    assert "深入" in scan.zh_ngrams("深入。深入") and "入深" not in scan.zh_ngrams("深入。深入")

    normalized = scan.excess_tables(Counter(alpha=2, beta=2), Counter(alpha=1, beta=1), 10, 1)
    assert all(row["ratio"] == 1 for row in normalized["seen"]), "Different corpus sizes need rates"
    unequal = scan.excess_tables(Counter(alpha=2, beta=2), Counter(alpha=1, beta=9), 10, 1)
    assert next(row for row in unequal["seen"] if row["token"] == "alpha")["ratio"] == 5
    no_baseline = scan.excess_tables(Counter(alpha=3), Counter(), 10, 2)
    assert no_baseline["n_ref"] == 0 and not no_baseline["baseline"]
    assert no_baseline["repeated"][0]["ref"] is None and no_baseline["repeated"][0]["ratio"] is None

    boundary_hits, _ = scan.lexical_candidates(
        [(Path("boundary.txt"), "delve DELVE delved undelve delve_like delve-like")],
        lexicon, "en", "general", 10)
    assert next(hit for hit in boundary_hits if hit["id"] == "delve")["count"] == 2
    top_hits, total_hits = scan.lexical_candidates([(Path("draft.txt"), cleaned)], lexicon, "en", "general", 1)
    assert top_hits[0]["id"] == "carbon" and top_hits[0]["count"] == 4 and total_hits == 3
    all_hits, _ = scan.lexical_candidates([(Path("draft.txt"), cleaned)], lexicon, "en", "general", 20)
    delve = next(hit for hit in all_hits if hit["id"] == "delve")
    assert delve["count"] == 2 and [hit["line"] for hit in delve["occurrences"]] == [1, 4]
    assert delve["sources"] == ["fixture"] and delve["review"] and delve["preserve"]
    ecology_hits, _ = scan.lexical_candidates([(Path("draft.txt"), cleaned)], lexicon, "en", "ecology", 20)
    assert {"carbon", "delve", "single", "ecology"} == {hit["id"] for hit in ecology_hits}
    zh_hits, _ = scan.lexical_candidates([(Path("draft.txt"), "深入。深入")], lexicon, "zh", "general", 20)
    assert zh_hits[0]["id"] == "zh" and zh_hits[0]["count"] == 2

    with tempfile.TemporaryDirectory(prefix="easyunslop-check-") as temporary:
        root = Path(temporary)
        target, dictionary, output = root / "draft.md", root / "lexicon.json", root / "scan.json"
        target.write_text(manuscript, encoding="utf-8")
        dictionary.write_text(json.dumps(lexicon), encoding="utf-8")
        base = ["--target", str(target), "--lexicon", str(dictionary)]

        def run(*arguments):
            stdout, stderr = io.StringIO(), io.StringIO()
            with redirect_stdout(stdout), redirect_stderr(stderr):
                code = scan.main(base + list(arguments))
            return code, stdout.getvalue(), stderr.getvalue()

        code, report, error = run("--json", str(output))
        assert code == 0, error
        result = json.loads(output.read_text(encoding="utf-8"))
        assert result["reference_files"] == [] and not result["blocks"]["英文单词"]["baseline"]
        assert next(row for row in result["blocks"]["英文单词"]["repeated"] if row["token"] == "carbon")["target"] == 4
        assert "不计算 AI 概率" in report and "领域术语" in report
        code, _, error = run("--min-count", "99", "--json", str(output))
        assert code == 0, error
        result = json.loads(output.read_text(encoding="utf-8"))
        assert result["blocks"]["英文单词"]["repeated"] == []
        assert next(hit for hit in result["lexical_candidates"] if hit["id"] == "single")["count"] == 1

        references = root / "references"
        references.mkdir()
        alpha, beta = references / "alpha.txt", references / "beta.md"
        alpha.write_text("alpha", encoding="utf-8")
        beta.write_text("beta", encoding="utf-8")
        (references / "README.txt").write_text("artifactnoise alpha beta", encoding="utf-8")
        (references / "ignored.csv").write_text("artifactnoise", encoding="utf-8")
        (references / "zh.txt").write_text("气候变化影响森林生态系统。", encoding="utf-8")
        (references / "empty.md").write_text("```text\nartifactnoise\n```", encoding="utf-8")
        (references / "broken.txt").write_bytes(b"\xff\xfe\x00")
        code, _, error = run("--ref", str(references), "--json", str(output))
        assert code == 0, error
        result = json.loads(output.read_text(encoding="utf-8"))
        assert set(result["reference_files"]) == {str(alpha), str(beta)}
        assert result["blocks"]["英文单词"]["n_ref"] == 2
        assert result["blocks"]["英文二三元词组"]["n_ref"] == 0, "References cannot join across files"
        assert any("语言不匹配" in warning for warning in result["warnings"])
        assert any("无法读取" in warning for warning in result["warnings"])
        assert any("清洗后无正文" in warning for warning in result["warnings"])
        assert any("仅 2 个统计单位" in warning for warning in result["warnings"])

        empty_ref = root / "empty-ref"
        empty_ref.mkdir()
        code, _, error = run("--ref", str(empty_ref), "--json", str(output))
        assert code == 0 and "没有有效" in error
        code, _, error = run("--profile", "unknown")
        assert code == 2 and "未知 profile" in error
        code, _, error = run("--top", "0")
        assert code == 2 and "正整数" in error

        for protected in (target, dictionary, alpha):
            original = protected.read_bytes()
            arguments = ["--out", str(protected)]
            if protected == alpha:
                arguments += ["--ref", str(references)]
            code, _, error = run(*arguments)
            assert code == 2 and "不能覆盖" in error
            assert protected.read_bytes() == original, f"Protected input changed: {protected}"
        code, _, error = run("--out", str(output), "--json", str(output))
        assert code == 2 and "不能覆盖" in error

        blank = root / "blank.txt"
        blank.write_text("", encoding="utf-8")
        code, _, error = run("--target", str(blank))
        assert code == 2 and "目标为空" in error
        damaged = root / "damaged.json"
        damaged.write_text('{"version":1,"sources":[],"entries":[]}', encoding="utf-8")
        code, _, error = run("--lexicon", str(damaged))
        assert code == 2 and "词库无效" in error
        assert target.read_text(encoding="utf-8") == manuscript, "Diagnostics must leave the draft intact"

    print("PASS: lexical scan, cleaning, profiles, normalized reference rates, and input protection")


if __name__ == "__main__":
    main()
