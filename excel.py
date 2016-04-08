#coding: utf8

from openpyxl import Workbook
from openpyxl.drawing.image import Image
from openpyxl.styles import PatternFill, Border, Side, Alignment, Protection, Font, colors


def writetoxlsx(filenamexlsx1, otdtofile,otdtofileint,fioxls,fioxlsint,monthtoxls,monthtoxlsint,
                datetoxls,datetoxlsint,overworkxl,overworkxl1,overworkxl2,overworkxl3, dutyxl, dutyxl1,
                dutyxl2,travelxl, travelxl1,travelxl2,travelxl3 , repairxl, ofdayxl ):
    filenamexlsx = filenamexlsx1 + '.xlsx'
    wb = Workbook()
    ws = wb.active

    font = Font(name='Calibri', size=11, bold=False, italic=False, vertAlign=None, underline='none',
                strike=False, color='FF000000')


    fill = PatternFill(fill_type=None, start_color='FFFFFFFF', end_color='FF000000')

    border = Border(
        left=Side(border_style=None, color='FF000000'),
        right=Side(border_style=None, color='FF000000'),
        top=Side(border_style=None, color='FF000000'),
        bottom=Side(border_style=None, color='FF000000'),
        diagonal=Side(border_style=None, color='FF000000'),
        diagonal_direction=0,
        outline=Side(border_style=None, color='FF000000'),
        vertical=Side(border_style=None, color='FF000000'),
        horizontal=Side(border_style=None, color='FF000000'))

    alignment = Alignment(horizontal='general', vertical='bottom', text_rotation=0, wrap_text=False,
                      shrink_to_fit=False, indent=0)

    number_format = 'General'

    protection = Protection(locked=True, hidden=False)

    a1 = ws['K14']
    d4 = ws['L16']
    ft = Font(color=colors.RED)
    a1.font = ft
    d4.font = ft
    def borderfunc(ws1,tx,rx,bx,lx ):
        if tx == 1:
            t = Border(top=Side(border_style='hair'))
        else:
            t = Border(top=Side(border_style='medium'))
        if rx ==1:
            r = Border(top=Side(border_style='hair'))
        else:
            r = Border(top=Side(border_style='medium'))
        if bx == 1:
            b = Border(top=Side(border_style='hair'))
        else:
            b = Border(top=Side(border_style='medium'))
        if lx == 1:
            l = Border(top=Side(border_style='hair'))
        else:
            l = Border(top=Side(border_style='medium'))
        wsx =ws[ws1]
        bordercell = [t,r,b,l]
        for i in bordercell:
            print(wsx.border)
 #           wsx.border = bordercell[i]
 #           wsx.border = bordercell[i+1]
 #           wsx.border = bordercell[i + 2]
 #           wsx.border = bordercell[i + 3]
    borderfunc('D30',1,2,2,1)
    b16 = ws['B16']
    b16border = Border(left=Side(border_style='medium'),
                       bottom=Side(border_style='medium'),
                       top=Side(border_style='medium'))
    b16.border = b16border

    d16 = ws['D16']
    d16border = Border(right=Side(border_style='hair'))
    d16.border = d16border

    b18 = ws['B18']
    b18border = Border(bottom=Side(border_style='medium'))
    b18.border = b18border

    b30 = ws['B30']
    b30border = Border( left=Side(border_style='hair'),
                        right = Side(border_style='dotted'),
                        bottom = Side(border_style='dashed'),
                        top =Side(border_style='mediumDashDotDot'))
    b30.border = b30border
    b32 = ws['B32']
    b32border = Border(left=Side(border_style='thick'),
                       right=Side(border_style='slantDashDot'),
                       bottom=Side(border_style='mediumDashDot'),
                       top=Side(border_style='medium'))
    b32.border = b32border

    b34 = ws['B34']
    b34border = Border(left=Side(border_style='dashDotDot'),
                       right=Side(border_style='dashDot'),
                       bottom=Side(border_style='mediumDashed'),
                       top=Side(border_style='double'))
    b34.border = b34border

    b36 = ws['B36']
    b36border = Border(left=Side(border_style='dashDotDot'),
                       right=Side(border_style='dashDot'),
                       bottom=Side(border_style='mediumDashed'),
                       top=Side(border_style='double'))
    b36.border = b36border

    b38 = ws['B38']
    b38border = Border(left=Side(border_style='dashDotDot'),
                       right=Side(border_style='dashDot'),
                       bottom=Side(border_style='mediumDashed'),
                       top=Side(border_style='double'))
    b38.border = b38border

    b40 = ws['B40']
    b40border = Border(left=Side(border_style='thin'))
    b40.border = b40border
    #   dotted mediumDashDotDot dashed thick slantDashDot hair mediumDashDot medium dashDotDot dashDot
#   mediumDashed double thin

    print("badabum")
    ws.column_dimensions["E"].width = 1.6
    ws.column_dimensions["H"].width = 30.0
    ws.column_dimensions["F"].width = 20.0
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
    ws.merge_cells('B1:I1')




    ws.title = "Бланк зарплаты"
    ws['C7'] = otdtofile
    ws['C9'] = fioxls
    ws['C11'] = monthtoxls
    ws['C13'] = datetoxls
    ws['F7'] = otdtofileint
    ws['F9'] = fioxlsint
    ws['F11'] = monthtoxlsint
    ws['F13'] = datetoxlsint
    ws['B16'] = overworkxl
    ws['E16'] = overworkxl1
    ws['E17'] = overworkxl2
    ws['E18'] = overworkxl3
    ws['B19'] = dutyxl
    ws['E19'] = dutyxl1
    ws['E20'] = dutyxl2
    ws['B21'] = travelxl
    ws['E21'] = travelxl1
    ws['E22'] = travelxl2
    ws['E23'] = travelxl3
    ws['B24'] = repairxl
    ws['B25'] = ofdayxl

    header = Image('header1.png')
    ws.add_image(header, 'B1')
    ws.column_dimensions["A"].width = 1.29
    wb.save(filename = filenamexlsx)

writetoxlsx("gomoraz", "Отдел","IT", "ФИО","Шафигуллин Ильфат Ульфатович", 'Отчетный месяц', "Апрель",
            'Дата заполнения', "Какая то дата", 'Переработки (часы)', 'х1, включая во время дежурств',
            'х1,5','х2','Дежурства','Полные (недели)', 'Хвосты (руб)','Проезд','Метро (20р.)', 'Автобус (20р.)',
            'Авто (км)', 'Ремонт электроники', 'Прогулы (ч.)')