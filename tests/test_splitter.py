import os
from pathlib import Path
from PyPDF2 import PdfWriter, PdfReader
from pdfsplitter.splitter import split_pdf

def create_pdf(path: Path, pages: int = 2) -> None:
    writer = PdfWriter()
    for _ in range(pages):
        writer.add_blank_page(width=72, height=72)
    with open(path, "wb") as fh:
        writer.write(fh)

def test_split_pdf(tmp_path: Path):
    input_pdf = tmp_path / "input.pdf"
    create_pdf(input_pdf)
    output_dir = tmp_path / "out"
    split_pdf(str(input_pdf), str(output_dir))

    files = sorted(output_dir.glob("page_*.pdf"))
    assert len(files) == 2
    for file in files:
        with open(file, "rb") as fh:
            reader = PdfReader(fh)
            assert len(reader.pages) == 1
