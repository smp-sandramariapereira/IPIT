#!/usr/bin/env python3
"""Verifica caminhos relativos usados em Markdown e HTML."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
MD_LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
HTML_LINK = re.compile(r"(?:href|src)=[\"']([^\"']+)[\"']", re.IGNORECASE)
SKIP_PREFIXES = ("http://", "https://", "mailto:", "tel:", "data:", "javascript:")


def candidates(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    if path.suffix == ".md":
        return MD_LINK.findall(text)
    return HTML_LINK.findall(text)


def resolve(source: Path, raw: str) -> Path | None:
    value = raw.strip().split()[0].strip("<>\"")
    if not value or value.startswith("#") or value.startswith(SKIP_PREFIXES):
        return None
    parsed = urlsplit(value)
    relative = unquote(parsed.path)
    if not relative:
        return None
    return (source.parent / relative).resolve()


def main() -> int:
    errors: list[str] = []
    files = sorted(ROOT.rglob("*.md")) + sorted(ROOT.rglob("*.html"))
    files = [p for p in files if ".git" not in p.parts]
    for source in files:
        for raw in candidates(source):
            target = resolve(source, raw)
            if target is not None and not target.exists():
                errors.append(f"{source.relative_to(ROOT)} -> {raw}")
    if errors:
        print("Links internos inexistentes:")
        print("\n".join(f"- {item}" for item in errors))
        return 1
    print(f"Links internos verificados em {len(files)} arquivos.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
