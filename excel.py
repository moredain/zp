#coding: utf8

from openpyxl import Workbook
from openpyxl.compat import range
from openpyxl.compat import range

def writetoxlsx(filenamexlsx1, buffer):
#    filenamexlsx = filenamexlsx1+'.xlsx'
    filenamexlsx = "gomoraz" + '.xlsx'
    wb = Workbook()
    ws = wb.active
    ws.title = "Бланк зарплаты"
    ws['F5'] = "Рустемович"
    wb.save(filename = filenamexlsx)