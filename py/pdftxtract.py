#!/usr/bin/env python3
"""
PDFtxtract.py
=============
Author: dfx
Usage: ./pdftxtract.py [source-file]
Dependencies: pdftotext, poppler (more info on https://pypi.org/project/pdftotext/)
"""

try:
  import pdftotext
except ImportError:
  print("This script requires pdftotext to be installed.")
  print("Run [pip install pdftotext] and try again.")
  print("\nMore info: https://pypi.org/project/pdftotext/")
  quit()

from sys import argv

def main():
  if (len(argv) <= 1):
    print("USAGE:\n: ./pdftxtract.py [source.pdf]")
    print("or")
    print(": python3 pdftxtract.py [source.pdf]")
    quit()
  else:
    try:
      with open(argv[1], "rb") as file:
        pdf = pdftotext.PDF(file)

      # Text extraction logic
      text = "".join(pdf) # Extract all text
      print(text)

    except FileNotFoundError:
      print("{0} does not exist.".format(argv[1]))
      quit()

if __name__ == "__main__":
  main()
