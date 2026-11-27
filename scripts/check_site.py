#!/usr/bin/env python3
"""Validate local links, page anchors and duplicate IDs in the static site."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.duplicates = set()
        self.links = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        element_id = attrs.get("id")
        if element_id:
            if element_id in self.ids:
                self.duplicates.add(element_id)
            self.ids.add(element_id)
        for attribute in ("href", "src"):
            value = attrs.get(attribute)
            if value:
                self.links.append(value)


def target_for(page: Path, url_path: str) -> Path:
    decoded_path = unquote(url_path)
    # Root-relative website URLs (for example href="/") resolve from the
    # static document root, not from the runner filesystem root.
    if decoded_path.startswith("/"):
        target = (ROOT / decoded_path.lstrip("/")).resolve()
    else:
        target = (page.parent / decoded_path).resolve()
    if target.is_dir():
        target = target / "index.html"
    elif not target.suffix and not target.exists():
        target = target / "index.html"
    return target


def main() -> int:
    pages = sorted(ROOT.rglob("*.html"))
    parsed = {}
    errors = []

    for page in pages:
        parser = PageParser()
        parser.feed(page.read_text(encoding="utf-8"))
        parsed[page.resolve()] = parser
        for duplicate in sorted(parser.duplicates):
            errors.append(f"{page.relative_to(ROOT)}: duplicate id #{duplicate}")

    for page in pages:
        parser = parsed[page.resolve()]
        for raw_url in parser.links:
            parts = urlsplit(raw_url)
            if parts.scheme or parts.netloc or raw_url.startswith("//"):
                continue
            target = target_for(page, parts.path) if parts.path else page.resolve()
            if not target.is_file():
                errors.append(f"{page.relative_to(ROOT)}: missing local target {raw_url}")
                continue
            if parts.fragment and target.suffix.lower() == ".html":
                target_parser = parsed.get(target.resolve())
                if target_parser is None:
                    target_parser = PageParser()
                    target_parser.feed(target.read_text(encoding="utf-8"))
                    parsed[target.resolve()] = target_parser
                fragment = unquote(parts.fragment)
                if fragment not in target_parser.ids:
                    errors.append(
                        f"{page.relative_to(ROOT)}: missing anchor "
                        f"#{fragment} in {target.relative_to(ROOT)}"
                    )

    if errors:
        print("Static site validation failed:")
        for error in errors:
            print(f" - {error}")
        return 1

    print(f"Static site validation passed: {len(pages)} HTML pages checked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
