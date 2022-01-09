from PyPDF2.generic import TextStringObject, NameObject
from PyPDF2.pdf import PdfFileReader, PdfFileWriter, ContentStream
from PyPDF2.utils import b_

import pikepdf

def decrypt(inFile, outFile, password):
  pdf = pikepdf.open(inFile, password=password)
  pdf.save(outFile)
  
def remove_watermark(in_file, out_file, watermark=''):
  source = PdfFileReader(open(in_file, 'rb'))
  output = PdfFileWriter()
  
  for page in range(source.getNumPages()):
    page = source.getPage(page)
    content_object = page["\Contents"].getObject()
    content = ContentStream(content_object, source)
    
    for operands, operator in content.operations:
      if operator == b_("Tj") or operator == b_("TJ"):
        # TODO: add logic here if you only want to replace specific strings
        # like comparing with the passed watermark and only removing then
        operands[0] = TextStringObject(' ')
        
    page.__setitem__(NameObject('\Contents'), content)
    output.addPage(page)
  
  output_stream = open(out_file, 'wb')
  output.write(output_stream)
  output_stream.close()
  
                   
