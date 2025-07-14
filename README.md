# pdfsplitter

A simple command line tool to split a PDF into individual pages.

## Installation

This project requires Python 3.8 or higher. Install the package using pip:

```bash
pip install .
```

For development you can install in editable mode:

```bash
pip install -e .
```

## Usage

After installation you can run the splitter from the command line:

```bash
pdfsplitter INPUT_PDF OUTPUT_FOLDER
```

This will create one PDF per page of `INPUT_PDF` inside `OUTPUT_FOLDER`.
