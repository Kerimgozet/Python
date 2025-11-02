from pdf2docx import Converter

pdf_file="unique-tower-139460.pdf"
docx_file="unique-tower-139460.docx"

cv=Converter(pdf_file=pdf_file)
cv.convert(docx_file=docx_file)
cv.close()