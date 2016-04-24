#coding: utf8
import sys

from datetime import datetime
import excel2

from PyQt5.QtCore import pyqtSlot, QDateTime
from PyQt5.QtWidgets import QApplication, QDialog, QDateEdit,QDateTimeEdit
from PyQt5.uic import loadUiType

app = QApplication(sys.argv)
app.setApplicationName('pyqt3')
form_class, base_class = loadUiType('window.ui')


class MainWindow(QDialog, form_class):
  def __init__(self, *args):
      super(MainWindow, self).__init__(*args)

      self.setupUi(self)
#-----------------------------------------------------#
#   Определение текущей даты

      self.dateEdit.setDateTime(QDateTime.currentDateTime())

#-----------------------------------------------------#
#   Составление имени файла

      now = datetime.today()
      tomonth = datetime.strftime(now,'%m')
      monthint=int(tomonth)
      nowstr = str(monthint)
      print(nowstr)
      user = self.label_10.text()
      usermod = user.replace(' ','-')
      print("user =" + usermod)
      filenamenow =datetime.strftime(now,'%Y-%m-%d') +"_"+usermod + ".txt"
      datetoday = datetime.strftime(now, '%Y-%m-%d')
      print( "filename =" + filenamenow )
#-----------------------------------------------------#
#   Определение отдела
      tootdel = self.label_14.text()
      print(tootdel)
#-----------------------------------------------------#
#   Определение текущего месяца
      self.comboBox.setCurrentIndex(monthint-1)
      thismonth = self.comboBox.currentText()
      print(thismonth)
# -----------------------------------------------------#

#-----------------------------------------------------#
#   Пишем в файл

#   Нижняя таблица ширина 75, высота 25
#   Прикинем размер таблиц.

#   Верхняя таблица высота 7, ширина = граница таблицы + 3 пробела + ширина самого
#       широкого поля первой колонки  + 3 пробела + граница таблицы +  3 пробела +
#       + ширина самого широкого поля второй колонки + 3 пробела + граница таблицы

#   Вторая таблица составляется аналогично, с добавлением третьего поля

      otdeltofile = self.label_8.text()
      fiotofile = self.label_9.text()
      monthtofile = self.label_13.text()
      datetofile = self.label_11.text()
      overworktofile = self.label_3.text()
      x1tofile = self.label_2.text()
      x15tofile = self.label_15.text()
      x2tofile = self.label_12.text()
      dutytofile = self.label_4.text()
      fulldutytofile = self.label_16.text()
      remaindertofile = self.label_18.text()
      traveltofile = self.label_23.text()
      subwaytofile = self.label_19.text()
      bustofile = self.label_20.text()
      cartofile = self.label_21.text()
      repairstofile = self.label_24.text()
      dayofftofile = self.label_5.text()
      x1tofileequal= self.lineEdit.text()
      x15tofileequal = self.lineEdit_6.text()
      x2tofileequal = self.lineEdit_7.text()
      fulldutytofileequal = self.lineEdit_2.text()
      remaindertofileequal = self.lineEdit_8.text()
      subwaytofileequal = self.lineEdit_9.text()
      bustofileequal = self.lineEdit_10.text()
      cartofileequal = self.lineEdit_11.text()
      repairstofileeequal = self.lineEdit_12.text()
      dayofftofileequal = self.lineEdit_3.text()

      len11 = len(otdeltofile)
      len12 = len(tootdel)
      len21 = len(fiotofile)
      len22 = len(user)
      len31 = len(monthtofile)
      len32 = len(thismonth)
      len41 = len(datetofile)
      len42 = len(datetime.strftime(now,'%y-%m-%d'))

      len5 = len(overworktofile)
      len511 = len(x1tofile)
      len512 = len(x15tofile)
      len513 = len(x2tofile)
      len521 = len(x1tofileequal)
      len522 = len(x15tofileequal)
      len523 = len(x2tofileequal)

      len6 = len(dutytofile)
      len611 = len(fulldutytofile)
      len612 = len(remaindertofile)
      len621 = len(fulldutytofileequal)
      len622 = len(remaindertofileequal)

      len7 = len(traveltofile)
      len711 = len(subwaytofile)
      len712 = len(bustofile)
      len713 = len(cartofile)
      len721 = len(subwaytofileequal)
      len722 = len(bustofileequal)
      len723 = len(cartofileequal)

      len8 = len(repairstofile)
      len82 = len(repairstofileeequal)

      len9 = len(dayofftofile)
      len92 = len(dayofftofileequal)

      listwidth11 = [len11,len21,len31,len41]
      listwidth12 = [len12,len22,len32,len42]
      listwidth11max = max(listwidth11)
      listwidth12max = max(listwidth12)
      intervalskrau = 3

      listwidth21 = [len5, len6, len7, len8,len9]
      listwidth21max = max(listwidth21)
      listwidth22 = [len511,len512,len513,len611,len612,len711,len712,len713]
      listwidth22max = max(listwidth22)
      listwidth23 = [len521,len522,len523,len621,len622,len721,len722,len723, len82,len92]
      listwidth23max = max(listwidth23)
      borderleft = '|'
      probel = ' '

      def dopoln11(anytext):
          anytextmod = anytext + probel*(listwidth11max-len(anytext))
          return anytextmod

      def dopoln12(anytext):
          anytextmod = anytext + probel * (listwidth12max - len(anytext))
          return anytextmod

      def dopoln21(anytext):
          anytextmod = anytext + probel * (listwidth21max - len(anytext))
          return anytextmod

      def dopoln22(anytext):
          anytextmod = anytext + probel * (listwidth22max - len(anytext))
          return anytextmod

      def dopoln23(anytext):
          anytextmod = anytext + probel * (listwidth23max - len(anytext))
          return anytextmod
      sleva = probel*intervalskrau
      left = borderleft + sleva
      right =   sleva + borderleft
      between =  sleva + borderleft + sleva



      row12 = left + dopoln11(otdeltofile) +  between + dopoln12(tootdel) + right

      table11width = len(row12)
      table111border = "=" * table11width
      table112border = '-' * table11width

      print(table111border)
      print(row12)
      print(table112border)
      row14 = left + dopoln11(fiotofile) + between + dopoln12(user) + right
      print(row14)
      print(table112border)
      row16 = left + dopoln11(monthtofile) + between + dopoln12(thismonth) + right
      print(row16)
      print(table112border)
      row18 = left + dopoln11(datetofile) + between + dopoln12(datetoday) + right
      print(row18)
      print(table111border)

# -----------------------------------------------------#
      row21 = left + dopoln21(probel) + between + dopoln22(x1tofile) + between\
              + dopoln23(x1tofileequal) + right
      table12width = len(row21)
      table121border = "=" * table12width
      table122border = "-"+ probel*(listwidth21max + 6) +"-"*(table12width-len("-"+ probel*(listwidth21max + 6)))
      print(table121border)
      print(row21)
      print(table122border)
      row22 = left + dopoln21(overworktofile) + between + dopoln22(x15tofile) \
              + between + dopoln23(x15tofileequal) + right
      print(row22)
      print(table122border)
      row23 = left + dopoln21(probel) + between + dopoln22(x2tofile) + between \
              + dopoln23(x2tofileequal) + right
      print(row23)
      print(table121border)
      print(table121border)
      row24 = left + dopoln21(dutytofile) + between + dopoln22(fulldutytofile) \
              + between + dopoln23(fulldutytofileequal) + right
      print(row24)
      print(table122border)
      row25 = left + dopoln21(probel) + between + dopoln22(remaindertofile) \
              + between + dopoln23(remaindertofileequal) + right
      print(row25)
      print(table121border)
      print(table121border)
      row26 = left + dopoln21(probel) + between + dopoln22(subwaytofile) \
              + between + dopoln23(subwaytofileequal) + right
      print(row26)
      print(table122border)
      row27 = left + dopoln21(traveltofile) + between + dopoln22(bustofile) \
              + between + dopoln23(bustofileequal) + right
      print(row27)
      print(table122border)
      row28 = left + dopoln21(probel) + between + dopoln22(cartofile) + between \
              + dopoln23(cartofileequal) + right
      print(row28)
      print(table121border)
      print(table121border)
      row29 = left + dopoln21(repairstofile) + between + dopoln22(probel) + between \
              + dopoln23(repairstofileeequal) + right
      print(row29)
      print(table121border)
      print(table121border)
      row210 = left + dopoln21(dayofftofile) + between + dopoln22(probel) + between \
               + dopoln23(dayofftofileequal) + right
      print(row210)
      print(table121border)
      mytext =[table112border, row12,table112border,row14,table112border,row16,table112border,
               row18,table112border,probel,probel,table121border,row21,table122border,row22,
               table122border,row23,table121border,table121border,row24,table122border,row25,
               table121border,table121border,row26,table122border,row27,table122border,row28,
               table121border,table121border,row29,table121border,table121border,row210,
               table121border]

#      def writetofile(mytext1,filename1):
#          workwithfile = open(filename1,"w")
#          i =0
#          for pishem in mytext1:
#              workwithfile.write(mytext1[i] +'\r\n')
#              i = i + 1
#          workwithfile.close()
#      writetofile(mytext,filenamenow)

#-----------------------------------------------------#
form = MainWindow()
form.setWindowTitle('Бланк зарплаты')
form.show()
sys.exit(app.exec_())







