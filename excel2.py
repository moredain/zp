#coding: utf8

from openpyxl import Workbook
from openpyxl.styles import Font, colors
from openpyxl import load_workbook


def writetoxlsx(filetosave,otdel, fio,month,date,x1,x15,x2,duty1,duty2,repair,dayoff,metro,bus,car):

    filenamexlsx ='temp/usertemp/'+filetosave + '.xlsx'
#    wb = Workbook()
    wb = load_workbook("temp/template.xlsx")
    ws = wb.active

    ws.title = "Бланк зарплаты"
    ws['D6'] = otdel
    ws['D8'] = fio
    ws['D10'] = month
    ws['D12'] = date

    ws['G14'] = x1
    ws['G15'] = x15
    ws['G16'] = x2
    ws['G17'] = duty1
    ws['G18'] = duty2
    ws['G19'] = repair
    ws['G20'] = dayoff
    ws['G21'] = metro
    ws['G22'] = bus
    ws['G23'] = car

    wb.save(filename = filenamexlsx)

writetoxlsx("gomoraz","IT","Шафигуллин Ильфат Ульфатович","Апрель","Какая то дата",'123','321','555','666','777',
            '555','123','111','123','233')