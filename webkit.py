import sys
import html_generator

from PyQt5.QtCore import QUrl,QFileInfo

from PyQt5.QtWidgets import QApplication

from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtWebKitWidgets import QWebView

app1 = QApplication(sys.argv)

web = QWebView()


link =QUrl.fromLocalFile(QFileInfo("bootstrap_mod/index.html").absoluteFilePath())

web.load(QUrl(link))


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