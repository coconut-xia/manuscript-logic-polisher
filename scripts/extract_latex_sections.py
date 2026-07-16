#!/usr/bin/env python3
"""Extract section-level prose and captions from a LaTeX manuscript."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


NON_PROSE_ENVIRONMENTS = (
    "figure",
    "figure*",
    "table",
    "table*",
    "longtable",
    "equation",
    "equation*",
    "align",
    "align*",
    "gather",
    "gather*",
    "multline",
    "multline*",
    "tikzpicture",
)

TEXT_WRAPPERS = (
    "textbf",
    "textit",
    "texttt",
    "textrm",
    "textsf",
    "emph",
    "underline",
    "runhead",
    "caprunhead",
)


def strip_comments(text: str) -> str:
    return re.sub(r"(?<!\\)%.*", "", text)


def remove_environment(text: str, environment: str) -> str:
    name = re.escape(environment)
    return re.sub(
        rf"\\begin\{{{name}\}}(?:\[[^]]*\])?.*?\\end\{{{name}\}}",
        "\n\n",
        text,
        flags=re.S,
    )


def balanced_arguments(text: str, command_pattern: str) -> list[str]:
    values: list[str] = []
    for match in re.finditer(command_pattern, text):
        start = text.find("{", match.start())
        if start < 0:
            continue
        depth = 0
        for index in range(start, len(text)):
            char = text[index]
            if char == "{" and (index == 0 or text[index - 1] != "\\"):
                depth += 1
            elif char == "}" and (index == 0 or text[index - 1] != "\\"):
                depth -= 1
                if depth == 0:
                    values.append(text[start + 1 : index])
                    break
    return values


def clean_prose(text: str) -> str:
    text = strip_comments(text)
    for environment in NON_PROSE_ENVIRONMENTS:
        text = remove_environment(text, environment)

    text = re.sub(r"\$\$.*?\$\$|\\\[.*?\\\]", " MATH ", text, flags=re.S)
    text = re.sub(r"(?<!\\)\$.*?(?<!\\)\$", " MATH ", text, flags=re.S)
    text = re.sub(
        r"\\(?:cite|citep|citet|ref|eqref|autoref|label|url|includegraphics)\*?(?:\[[^]]*\])?\{[^{}]*\}",
        " ",
        text,
    )
    text = re.sub(r"\\href\{[^{}]*\}\{([^{}]*)\}", r"\1", text)

    wrapper_pattern = r"\\(?:" + "|".join(TEXT_WRAPPERS) + r")\{([^{}]*)\}"
    previous = None
    while previous != text:
        previous = text
        text = re.sub(wrapper_pattern, r"\1", text)

    text = re.sub(r"\\(?:section|subsection|subsubsection)\*?\{[^{}]*\}", "\n\n", text)
    text = re.sub(r"\\begin\{[^{}]*\}|\\end\{[^{}]*\}", "\n\n", text)
    text = re.sub(r"\\[A-Za-z@]+\*?(?:\[[^]]*\])?", " ", text)
    text = text.replace("~", " ").replace("\\&", "&").replace("--", "-")
    text = text.replace("{", " ").replace("}", " ").replace("\\\\", "\n")

    paragraphs = []
    for paragraph in re.split(r"\n\s*\n", text):
        paragraph = re.sub(r"\s+", " ", paragraph).strip()
        if len(re.findall(r"[A-Za-z]+", paragraph)) >= 4:
            paragraphs.append(paragraph)
    return "\n\n".join(paragraphs) + ("\n" if paragraphs else "")


def slugify(title: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "_", title.lower()).strip("_")
    return slug or "section"


def extract_sections(text: str) -> list[tuple[str, str]]:
    matches = list(re.finditer(r"\\section\*?\{([^{}]+)\}", text))
    sections = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        sections.append((match.group(1).strip(), text[match.end() : end]))
    return sections


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="UTF-8 LaTeX source")
    parser.add_argument("output_dir", type=Path, help="Directory for extracted text files")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.input.is_file():
        raise SystemExit(f"File not found: {args.input}")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    raw = args.input.read_text(encoding="utf-8", errors="replace")
    written = []

    abstract = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", raw, flags=re.S)
    if abstract:
        path = args.output_dir / "abstract.txt"
        path.write_text(clean_prose(abstract.group(1)), encoding="utf-8")
        written.append({"title": "Abstract", "file": str(path)})

    used_slugs: dict[str, int] = {}
    for title, content in extract_sections(raw):
        base = slugify(title)
        used_slugs[base] = used_slugs.get(base, 0) + 1
        suffix = "" if used_slugs[base] == 1 else f"_{used_slugs[base]}"
        path = args.output_dir / f"{base}{suffix}.txt"
        path.write_text(clean_prose(content), encoding="utf-8")
        written.append({"title": title, "file": str(path)})

    captions = balanced_arguments(raw, r"\\caption(?:of\{[^{}]+\})?\s*\{")
    if captions:
        path = args.output_dir / "captions.txt"
        path.write_text("\n\n".join(clean_prose(value).strip() for value in captions) + "\n", encoding="utf-8")
        written.append({"title": "Captions", "file": str(path)})

    print(json.dumps({"source": str(args.input), "outputs": written}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
