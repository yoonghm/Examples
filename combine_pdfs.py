#!/usr/bin/env python3

## Description
# Combine multiple PDF files according to the file name sequence in filename.txt
# The output is named _OUTPUT.pdf

## Syntax
# combine_pdfs.py 

from PyPDF2 import PdfFileReader, PdfFileMerger

fname = "filename.txt"
outfn = "_OUTPUT.pdf"

merger = PdfFileMerger()

with open(fname) as f:
  files = f.read().splitlines()

for fn in files:
  print fn
  merger.append(PdfFileReader(fn), "rb")

merger.write(outfn)
