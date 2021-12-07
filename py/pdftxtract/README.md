# PDFtxtract

Author: dfx

## pdftxtract.py

A commmand line script to extract all text from a PDF file

Usage: ./pdftxtract.py [source-file.pdf]
Dependencies: libpdftxt

## libpdftxt

Extract all text from a PDF file using pdfplumber module.
Better compatibility than the libpdftxt_old module, but
the resulting output might not be great.

Usage: Import the module and call get_text(path-to-file)
Dependencies: pdfplumber (more info on https://pypi.org/project/pdfplumber/)

## libpdftxt_old

Extract all text from a PDF file using pdftotext module.
Relies on poppler, which can be a pain to install, but
parses the PDF without a problem.

Usage: Import the module and call get_text(path-to-file)
Dependencies: pdftotext, poppler (more info on https://pypi.org/project/pdftotext/)