# pdfsplitter

A simple command line tool to split a PDF into individual pages.

## Installation

This project requires Python 3.8 or higher. Install the dependencies using pip:

```bash
pip install PyPDF2
```

Alternatively, you can install the project in editable mode using the provided
`pyproject.toml`:

```bash
pip install -e .
```

## Usage

After installation you can run the splitter from the command line:

```bash
pdfsplitter INPUT_PDF OUTPUT_FOLDER
```

This will create one PDF per page of `INPUT_PDF` inside `OUTPUT_FOLDER`.
