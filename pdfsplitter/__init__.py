import os
from typing import Optional
import PyPDF2

__all__ = ["split_pdf"]

def split_pdf(input_pdf_path: str, output_folder: str) -> None:
    """Split *input_pdf_path* into single-page PDFs saved in *output_folder*."""
    with open(input_pdf_path, "rb") as input_pdf:
        reader = PyPDF2.PdfReader(input_pdf)
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        for i, page in enumerate(reader.pages, start=1):
            writer = PyPDF2.PdfWriter()
            writer.add_page(page)
            output_pdf_path = os.path.join(output_folder, f"page_{i}.pdf")
            with open(output_pdf_path, "wb") as out_fh:
                writer.write(out_fh)
            print(f"Created: {output_pdf_path}")

