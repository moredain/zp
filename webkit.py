import sys

from PyQt5.QtCore import QUrl, QObject,pyqtSignal

from PyQt5.QtWidgets import QApplication, QDialog

from PyQt5.QtPrintSupport import QPrintDialog, QPrinter, QPrintPreviewDialog, QPrinterInfo
from PyQt5.QtWebKitWidgets import QWebPage, QWebView
from PyQt5.QtWebKit import QWebSettings

app1 = QApplication(sys.argv)

web = QWebView()


web.load(QUrl('file:///home/umbrella/PycharmProjects/zp/bootstrap_mod/index.html'))


printer = QPrinter()
printer.setPageSize(QPrinter.A4)
printer.setOutputFormat(QPrinter.PdfFormat)
printer.setOutputFileName("file.pdf")

web.print(printer)
print('pdf generated')
QApplication.exit()
def convertIt():
        web.print(printer)
        print("Pdf generated")
        QApplication.exit()

web.loadFinished.connect(convertIt)
sys.exit(app1.exec_())