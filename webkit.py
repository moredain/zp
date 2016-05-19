import sys

from PyQt5.QtCore import QUrl, QObject,pyqtSignal

from PyQt5.QtWidgets import QApplication, QDialog

from PyQt5.QtPrintSupport import QPrintDialog, QPrinter, QPrintPreviewDialog, QPrinterInfo
from PyQt5.QtWebKitWidgets import QWebPage, QWebView

app1 = QApplication(sys.argv)

web = QWebView()

#local_url = QUrl.fromLocalFile('bootstrap_mod/example.html')
web.load(QUrl('file:///home/umbrella/PycharmProjects/zp/bootstrap_mod/example.html'))
web.setStyleSheet("qrc:/bootstrap_mod/example/bootstrap.min.css")
#view.settings().setUserStyleSheetUrl(QUrl.fromLocalFile("style.css"))
# web.show() можно показать страницу
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