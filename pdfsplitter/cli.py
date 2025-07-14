import argparse
from . import split_pdf

def main() -> None:
    parser = argparse.ArgumentParser(description="Split a multi-page PDF into individual pages.")
    parser.add_argument("input_pdf", help="Path to the input PDF file")
    parser.add_argument("output_folder", help="Folder to save the split PDFs")
    args = parser.parse_args()
    split_pdf(args.input_pdf, args.output_folder)

if __name__ == "__main__":
    main()

