import sys

from PyQt5.QtCore import QUrl, QObject,pyqtSignal

from PyQt5.QtWidgets import QApplication, QDialog

from PyQt5.QtPrintSupport import QPrintDialog, QPrinter, QPrintPreviewDialog, QPrinterInfo
from PyQt5.QtWebKitWidgets import QWebPage, QWebView

app1 = QApplication(sys.argv)

web = QWebView()
web.load(QUrl("yandex.ru"))
# web.show() можно показать страницу
printer = QPrinter()
printer.setPageSize(QPrinter.A4)
printer.setOutputFormat(QPrinter.PdfFormat)
printer.setOutputFileName("file.pdf")

def convertIt():
        web.print_(printer)
        print
        "Pdf generated"
        QApplication.exit()

convertIt()
#QObject.connect(web, SIGNAL("loadFinished(bool)"), convertIt)
#QObject.connect(web, SIGNAL("loadFinished(bool)"), convertIt)
sys.exit(app1.exec_())