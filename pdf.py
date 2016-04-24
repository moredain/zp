from openpyxl import load_workbook
from PyPDF2 import PdfFileReader, PdfFileWriter

wb = load_workbook("temp/template.xlsx")
ws = wb.active
output = PdfFileWriter()


output.addPage('hgjjkgjhgh')
output.addPage('jhkhjkhkjkjjkjkkkkk')

with open('newfile.pdf', 'wb') as f:
   output.write(f)