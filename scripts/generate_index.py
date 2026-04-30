#!/usr/bin/env python3
from __future__ import annotations

import re
from collections.abc import Iterator
from dataclasses import dataclass
from pathlib import Path

# =========================
# Configuration
# =========================


@dataclass(frozen=True)
class DocTypeConfig:
    name: str
    directory: Path
    index_file: Path
    start_marker: str
    end_marker: str
    title_prefix_pattern: re.Pattern[str]
    table_headers: list[str]


DOC_TYPES: list[DocTypeConfig] = [
    DocTypeConfig(
        name="ADR",
        directory=Path("docs/architecture/adr"),
        index_file=Path("docs/architecture/adr/index.md"),
        start_marker="<!-- ADR-INDEX:START -->",
        end_marker="<!-- ADR-INDEX:END -->",
        title_prefix_pattern=re.compile(r"^\s*ADR\s+\d{4}\s*:\s*", re.IGNORECASE),
        table_headers=["ADR", "Title", "Status", "Date", "Tags"],
    ),
    DocTypeConfig(
        name="RFC",
        directory=Path("docs/rfc"),
        index_file=Path("docs/rfc/index.md"),
        start_marker="<!-- RFC-INDEX:START -->",
        end_marker="<!-- RFC-INDEX:END -->",
        title_prefix_pattern=re.compile(r"^\s*RFC\s+\d{4}\s*:\s*", re.IGNORECASE),
        table_headers=["RFC", "Title", "Status", "Date", "Tags"],
    ),
]

FILENAME_RE = re.compile(r"^(?P<num>\d{4})-(?P<slug>.+)\.md$")
H1_RE = re.compile(r"^\s*#\s+(?P<title>.+?)\s*$", re.MULTILINE)
META_ROW_RE = re.compile(
    r"^\|\s*\*\*(?P<key>[^*]+)\*\*\s*\|\s*(?P<val>.*?)\s*\|?\s*$",
    re.MULTILINE,
)

IGNORED_FILES = {"README.md", "template.md", "index.md"}

# =========================
# Models
# =========================


@dataclass(frozen=True)
class IndexedDoc:
    number: int
    filename: str
    title: str
    date: str
    status: str
    tags: str


# =========================
# Parsing helpers
# =========================


def clean_cell(value: str) -> str:
    v = value.strip()
    v = v.replace("<br/>", " ").replace("<br />", " ")
    v = re.sub(r"\s+", " ", v)
    if len(v) >= 2 and v.startswith("`") and v.endswith("`"):
        v = v[1:-1].strip()
    return v


def parse_metadata(md: str) -> dict[str, str]:
    meta: dict[str, str] = {}
    for m in META_ROW_RE.finditer(md):
        meta[m.group("key").lower()] = clean_cell(m.group("val"))
    return meta


def parse_title(md: str, fallback: str, prefix_re: re.Pattern[str]) -> str:
    m = H1_RE.search(md)
    title = m.group("title").strip() if m else fallback
    return prefix_re.sub("", title).strip()


# =========================
# Indexing pipeline
# =========================


def iter_docs(directory: Path) -> Iterator[Path]:
    if not directory.exists():
        return
    for p in sorted(directory.glob("*.md")):
        if p.name in IGNORED_FILES:
            continue
        if FILENAME_RE.match(p.name):
            yield p


def load_doc(path: Path, cfg: DocTypeConfig) -> IndexedDoc:
    md = path.read_text(encoding="utf-8")
    m = FILENAME_RE.match(path.name)
    assert m, f"Invalid filename: {path.name}"

    number = int(m.group("num"))
    meta = parse_metadata(md)

    return IndexedDoc(
        number=number,
        filename=path.name,
        title=parse_title(md, path.stem, cfg.title_prefix_pattern),
        date=meta.get("date", ""),
        status=meta.get("status", ""),
        tags=meta.get("tags", ""),
    )


def generate_table(cfg: DocTypeConfig, records: list[IndexedDoc]) -> str:
    headers = cfg.table_headers
    sep = ["---"] * len(headers)

    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(sep) + " |",
    ]

    for r in records:
        link = f"[{r.number:04d}]({r.filename})"
        row = [
            link,
            r.title or "-",
            r.status or "-",
            r.date or "-",
            r.tags or "-",
        ]
        lines.append("| " + " | ".join(row) + " |")

    return "\n".join(lines)


def replace_between_markers(text: str, start: str, end: str, replacement: str) -> str:
    if start not in text or end not in text:
        raise RuntimeError(f"Missing markers:\n{start}\n{end}")
    before, rest = text.split(start, 1)
    _, after = rest.split(end, 1)
    return f"{before}{start}\n{replacement}\n{end}{after}"


# =========================
# Main
# =========================


def update_index(cfg: DocTypeConfig) -> None:
    if not cfg.index_file.exists():
        raise RuntimeError(f"Missing index file: {cfg.index_file}")

    records = [load_doc(p, cfg) for p in iter_docs(cfg.directory)]
    records.sort(key=lambda r: r.number)

    table = generate_table(cfg, records) if records else "_No records yet._"
    current = cfg.index_file.read_text(encoding="utf-8")
    updated = replace_between_markers(current, cfg.start_marker, cfg.end_marker, table)

    if updated != current:
        cfg.index_file.write_text(updated, encoding="utf-8")
        print(f"Updated {cfg.name} index → {cfg.index_file}")
    else:
        print(f"{cfg.name} index already up to date.")


def main() -> int:
    for cfg in DOC_TYPES:
        update_index(cfg)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
