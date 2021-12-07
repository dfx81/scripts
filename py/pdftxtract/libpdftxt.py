"""
libpdftxt.py
=============
Author: dfx
Usage: Import this module and call get_text(path-to-file)
Dependencies: pdfplumber (more info on https://pypi.org/project/pdfplumber/)
"""

try:
  import pdfplumber
except ImportError:
  print("This module requires pdfplumber to be installed.")
  print("Run [pip install pdfplumber] and try again.")
  print("\nMore info: https://pypi.org/project/pdfplumber/")
  quit()

def get_text(path):
  with pdfplumber.open(path) as pdf:
    # Text extraction logic
    text = ""

    for page in pdf.pages:
      text += page.extract_text()

    return text