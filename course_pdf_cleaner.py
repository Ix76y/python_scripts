from PyPDF2.generic import TextStringObject, NameObject
from PyPDF2.pdf import PdfFileReader, PdfFileWriter, ContentStream
from PyPDF2.utils import b_

import pikepdf

def decrypt(inFile, outFile, password):
  pdf = pikepdf.open(inFile, password=password)
  pdf.save(outFile)
  
