import sys
import html_generator

from PyQt5.QtCore import QUrl,QFileInfo

from PyQt5.QtWidgets import QApplication

from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtWebKitWidgets import QWebView

def PdfConverter(username):
        htmllink = "bootstrap_mod/"+username+".html"
        app1 = QApplication(sys.argv)

        web = QWebView()


        link =QUrl.fromLocalFile(QFileInfo(htmllink).absoluteFilePath())

        web.load(QUrl(link))

        printer = QPrinter()
        printer.setPageSize(QPrinter.A4)
        printer.setOutputFormat(QPrinter.PdfFormat)
        Pdf_Generated_Name=username+".pdf"
        printer.setOutputFileName(Pdf_Generated_Name)

        web.print(printer)
        QApplication.exit()
        def convertIt():
                web.print(printer)
                print("Pdf generated")
                QApplication.exit()

        web.loadFinished.connect(convertIt)
        sys.exit(app1.exec_())

PdfConverter("gopnik")