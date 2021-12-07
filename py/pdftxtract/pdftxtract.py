#!/usr/bin/env python3

"""
pdftxtract.py
=============
Author: dfx
Usage: ./pdftxtract.py [source-file.pdf]
Dependencies: libpdftxt, libpdftxt_old
"""

from sys import argv
import libpdftxt as pdf

def main():
  if (len(argv) <= 1):
    print("USAGE:\n: ./pdftxtract.py [source-file.pdf]")
    print("or")
    print(": python3 pdftxtract.py [source-file.pdf]")

  else:
    try:
      text = pdf.get_text(argv[1])

      if (text):
        print(text)

    except FileNotFoundError:
      print("{0} does not exist.".format(argv[1]))

if __name__ == "__main__":
  main()