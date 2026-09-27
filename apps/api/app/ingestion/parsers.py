"""File -> list of pages. One parser per format, chosen by MIME type."""
from dataclasses import dataclass, field
from typing import Protocol


@dataclass
class ParsedPage:
    page_number: int                     # 1-based; for non-paged formats use 1
    text: str
    headings: list[str] = field(default_factory=list)   # headings found on this page, in order


class Parser(Protocol):
    def parse(self, data: bytes) -> list[ParsedPage]: ...


class PdfParser:
    def parse(self, data: bytes) -> list[ParsedPage]:
        """TODO(M2): PyMuPDF (`fitz.open(stream=data, filetype="pdf")`).

        * page.get_text("text") for plain text
        * headings: use page.get_text("dict") and treat spans whose font size is
          clearly above the page's median (e.g. >1.2x) or bold as headings
        * stretch: if a page yields < 20 chars, it's probably scanned -> OCR fallback
        """
        raise NotImplementedError


class MarkdownParser:
    def parse(self, data: bytes) -> list[ParsedPage]:
        """TODO(M2): single page; headings = lines starting with '#'."""
        raise NotImplementedError


class TextParser:
    def parse(self, data: bytes) -> list[ParsedPage]:
        """TODO(M2): single page, no headings. Decode as UTF-8 with errors='replace'."""
        raise NotImplementedError


def get_parser(mime_type: str) -> Parser:
    """TODO(M2): map MIME -> parser; raise UnsupportedFileType for anything else.
    Stretch: DocxParser (python-docx), HtmlParser (selectolax / BeautifulSoup)."""
    raise NotImplementedError
