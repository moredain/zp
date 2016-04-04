#coding: utf8

from openpyxl import Workbook
from openpyxl.drawing.image import Image
from openpyxl.styles import (
    Font,
    Fill,
    GradientFill,
    PatternFill,
    Border,
    Alignment,
    Protection,
    HashableObject
    )

def writetoxlsx(filenamexlsx1, otdtofile,fioxls,monthtoxls,
                datetoxls):
#    filenamexlsx = filenamexlsx1+'.xlsx'
    filenamexlsx = filenamexlsx1 + '.xlsx'
    print(filenamexlsx)
    wb = Workbook()
    ws = wb.active


    ws.column_dimensions["E"].width = 1.6
    ws.merge_cells('C7:D7')
    ws.merge_cells('C9:D9')
    ws.merge_cells('F9:H9')
    ws.merge_cells('F11:H11')
    ws.merge_cells('F13:H13')
    ws.merge_cells('C11:D11')
    ws.merge_cells('C13:D13')
    ws.merge_cells('F7:H7')
    ws.merge_cells('B16:D18')
    ws.merge_cells('B19:D20')
    ws.merge_cells('B21:D23')
    ws.merge_cells('B24:D24')
    ws.merge_cells('B25:D25')
    ws.merge_cells('E16:G16')
    ws.merge_cells('E17:G17')
    ws.merge_cells('E18:G18')
    ws.merge_cells('E19:G19')
    ws.merge_cells('E20:G20')
    ws.merge_cells('E21:G21')
    ws.merge_cells('E22:G22')
    ws.merge_cells('E23:G23')
    ws.merge_cells('E24:G24')
    ws.merge_cells('E25:G25')
    ws.merge_cells('H16:I16')
    ws.merge_cells('H17:I17')
    ws.merge_cells('H18:I18')
    ws.merge_cells('H19:I19')
    ws.merge_cells('H20:I20')
    ws.merge_cells('H21:I21')
    ws.merge_cells('H22:I22')
    ws.merge_cells('H23:I23')
    ws.merge_cells('H24:I24')
    ws.merge_cells('H25:I25')

    ws.title = "Бланк зарплаты"
    ws['F5'] = "Рустем0вич"
    ws['C7'] = otdtofile
    ws['C9'] = fioxls
    ws['C11'] = monthtoxls
    ws['C13'] = datetoxls
    header = Image('header1.png')
    ws.add_image(header, 'B1')
    ws.column_dimensions["A"].width = 1.29
    wb.save(filename = filenamexlsx)

writetoxlsx("gomoraz", "Отдел", "ФИО", 'Отчетный месяц', 'Дата заполнения')