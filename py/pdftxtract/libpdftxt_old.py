"""
libpdftxt_old.py
=============
Author: dfx
Usage: Import this module and call get_text(path-to-file)
Dependencies: pdftotext, poppler (more info on https://pypi.org/project/pdftotext/)
"""

try:
  import pdftotext
except ImportError:
  print("This script requires pdftotext to be installed.")
  print("Run [pip install pdftotext] and try again.")
  print("\nMore info: https://pypi.org/project/pdftotext/")
  quit()

def get_text(path):
  with open(path, "rb") as file:
    pdf = pdftotext.PDF(file)

  # Text extraction logic
  text = "".join(pdf) # Extract all text

  return text