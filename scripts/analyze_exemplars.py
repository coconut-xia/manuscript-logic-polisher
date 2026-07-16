#!/usr/bin/env python3
"""Report aggregate surface-style statistics for English academic exemplars."""

from __future__ import annotations

import argparse
import json
import re
import statistics
from collections import Counter
from pathlib import Path
from typing import Iterable


TRANSITIONS = {
    "addition": ["additionally", "furthermore", "moreover", "in addition"],
    "contrast": ["however", "nevertheless", "nonetheless", "in contrast", "whereas", "although"],
    "cause_consequence": ["therefore", "thus", "consequently", "as a result", "because"],
    "example_evidence": ["for example", "for instance", "specifically", "indeed"],
    "comparison": ["similarly", "likewise", "compared with", "relative to"],
    "sequence": ["first", "second", "finally", "subsequently", "then"],
    "reformulation": ["in other words", "that is", "namely"],
    "limitation": ["despite", "although", "while", "notwithstanding"],
    "implication": ["suggesting that", "indicating that", "this implies", "these findings suggest"],
}

HEDGES = [
    "may", "might", "could", "appears", "appear", "suggests", "suggest", "likely",
    "potentially", "approximately", "generally", "relatively", "to our knowledge",
]

BOOSTERS = [
    "clearly", "demonstrates", "demonstrate", "establishes", "establish", "strongly",
    "markedly", "substantially", "robustly", "notably",
]

FIRST_PERSON = ["we", "our", "ours"]


def strip_markup(text: str, suffix: str) -> str:
    """Remove common Markdown/LaTeX markup while retaining prose approximately."""
    if suffix == ".tex":
        text = re.sub(r"(?<!\\)%.*", " ", text)
        text = re.sub(r"\\(?:cite|ref|label|eqref|autoref|url|href)\*?(?:\[[^]]*\])?\{[^{}]*\}", " ", text)
        text = re.sub(r"\\(?:begin|end)\{[^{}]*\}", " ", text)
        text = re.sub(r"\\[A-Za-z@]+\*?(?:\[[^]]*\])?", " ", text)
        text = text.replace("{", " ").replace("}", " ")
    if suffix == ".md":
        text = re.sub(r"```.*?```", " ", text, flags=re.S)
        text = re.sub(r"!??\[([^]]*)\]\([^)]*\)", r"\1", text)
        text = re.sub(r"^\s{0,3}#{1,6}\s+", "", text, flags=re.M)
        text = re.sub(r"[*_`>]", " ", text)
    return re.sub(r"[ \t]+", " ", text)


def split_sentences(text: str) -> list[str]:
    text = re.sub(r"\b(Fig|Eq|Ref|Dr|Mr|Ms|Prof)\.\s*", r"\1<prd> ", text)
    pieces = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9])", text)
    return [p.replace("<prd>", ".").strip() for p in pieces if len(p.split()) >= 3]


def word_tokens(text: str) -> list[str]:
    return re.findall(r"[A-Za-z]+(?:[-'][A-Za-z]+)*", text.lower())


def phrase_count(text: str, phrases: Iterable[str]) -> int:
    return sum(len(re.findall(r"(?<![A-Za-z])" + re.escape(p) + r"(?![A-Za-z])", text)) for p in phrases)


def percentile(values: list[int], fraction: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    index = max(0, min(len(ordered) - 1, round((len(ordered) - 1) * fraction)))
    return float(ordered[index])


def analyze(path: Path) -> dict:
    raw = path.read_text(encoding="utf-8", errors="replace")
    text = strip_markup(raw, path.suffix.lower())
    sentences = split_sentences(text)
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if len(word_tokens(p)) >= 5]
    words = word_tokens(text)
    sentence_lengths = [len(word_tokens(s)) for s in sentences]
    paragraph_lengths = [len(split_sentences(p)) for p in paragraphs]
    lower = text.lower()
    transition_counts = {category: phrase_count(lower, phrases) for category, phrases in TRANSITIONS.items()}
    passive_proxy = len(re.findall(r"\b(?:is|are|was|were|be|been|being)\s+(?:\w+ly\s+)?\w+(?:ed|en)\b", lower))
    scale = max(len(words), 1) / 1000

    return {
        "file": str(path),
        "words": len(words),
        "sentences": len(sentences),
        "paragraphs": len(paragraphs),
        "sentence_words": {
            "mean": round(statistics.mean(sentence_lengths), 2) if sentence_lengths else 0,
            "median": round(statistics.median(sentence_lengths), 2) if sentence_lengths else 0,
            "p90": round(percentile(sentence_lengths, 0.9), 2),
        },
        "paragraph_sentences_mean": round(statistics.mean(paragraph_lengths), 2) if paragraph_lengths else 0,
        "per_1000_words": {
            "transitions": {key: round(value / scale, 2) for key, value in transition_counts.items()},
            "hedges": round(phrase_count(lower, HEDGES) / scale, 2),
            "boosters": round(phrase_count(lower, BOOSTERS) / scale, 2),
            "first_person": round(phrase_count(lower, FIRST_PERSON) / scale, 2),
            "passive_proxy": round(passive_proxy / scale, 2),
        },
        "top_content_words": Counter(w for w in words if len(w) > 5).most_common(12),
    }


def aggregate(items: list[dict]) -> dict:
    total_words = sum(item["words"] for item in items)
    if not items:
        return {"files": 0, "words": 0}
    return {
        "files": len(items),
        "words": total_words,
        "mean_sentence_words": round(statistics.mean(item["sentence_words"]["mean"] for item in items), 2),
        "mean_paragraph_sentences": round(statistics.mean(item["paragraph_sentences_mean"] for item in items), 2),
        "mean_per_1000_words": {
            metric: round(statistics.mean(item["per_1000_words"][metric] for item in items), 2)
            for metric in ("hedges", "boosters", "first_person", "passive_proxy")
        },
    }


def to_markdown(report: dict) -> str:
    lines = ["# Exemplar surface-style report", "", "## Corpus", ""]
    corpus = report["corpus"]
    lines.extend([
        f"- Files: {corpus['files']}",
        f"- Words: {corpus['words']}",
        f"- Mean sentence length: {corpus.get('mean_sentence_words', 0)} words",
        f"- Mean paragraph length: {corpus.get('mean_paragraph_sentences', 0)} sentences",
        "",
        "## Per-file diagnostics",
        "",
    ])
    for item in report["documents"]:
        lines.extend([
            f"### {Path(item['file']).name}",
            "",
            f"- Words / sentences / paragraphs: {item['words']} / {item['sentences']} / {item['paragraphs']}",
            f"- Sentence words (mean / median / p90): {item['sentence_words']['mean']} / {item['sentence_words']['median']} / {item['sentence_words']['p90']}",
            f"- Hedges / boosters / first person / passive proxy per 1,000 words: {item['per_1000_words']['hedges']} / {item['per_1000_words']['boosters']} / {item['per_1000_words']['first_person']} / {item['per_1000_words']['passive_proxy']}",
            "- Transitions per 1,000 words: " + ", ".join(f"{k}={v}" for k, v in item["per_1000_words"]["transitions"].items()),
            "",
        ])
    lines.extend(["_Interpret these approximate surface measures manually; they are not prescriptive style rules._", ""])
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="+", type=Path, help="UTF-8 .txt, .md, or .tex exemplar files")
    parser.add_argument("--format", choices=("json", "markdown"), default="json")
    parser.add_argument("--output", type=Path, help="Write the report to this path instead of stdout")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    unsupported = [str(path) for path in args.files if path.suffix.lower() not in {".txt", ".md", ".tex"}]
    missing = [str(path) for path in args.files if not path.is_file()]
    if unsupported:
        raise SystemExit("Unsupported file type: " + ", ".join(unsupported))
    if missing:
        raise SystemExit("File not found: " + ", ".join(missing))

    documents = [analyze(path) for path in args.files]
    report = {"corpus": aggregate(documents), "documents": documents}
    rendered = json.dumps(report, ensure_ascii=False, indent=2) + "\n" if args.format == "json" else to_markdown(report)
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
