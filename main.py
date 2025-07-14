import argparse
import PyPDF2
import os

def split_pdf(input_pdf_path, output_folder):
    # Open the input PDF file
    with open(input_pdf_path, "rb") as input_pdf:
        reader = PyPDF2.PdfReader(input_pdf)
        total_pages = len(reader.pages)
        
        # Create the output folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        # Loop through all the pages and create individual PDFs
        for page_num in range(total_pages):
            writer = PyPDF2.PdfWriter()
            writer.add_page(reader.pages[page_num])
            
            # Save each page as a new PDF
            output_pdf_path = os.path.join(output_folder, f"page_{page_num + 1}.pdf")
            with open(output_pdf_path, "wb") as output_pdf:
                writer.write(output_pdf)
            print(f"Created: {output_pdf_path}")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Split a multi-page PDF into individual pages.")
    parser.add_argument("input_pdf", help="Path to the input PDF file")
    parser.add_argument("output_folder", help="Folder to save the split PDFs")

    # Parse the arguments
    args = parser.parse_args()

    # Call the split_pdf function with the arguments
    split_pdf(args.input_pdf, args.output_folder)

if __name__ == "__main__":
    main()
