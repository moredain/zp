import sys

from PyQt5.QtCore import QUrl, QObject,pyqtSignal

from PyQt5.QtWidgets import QApplication, QDialog

from PyQt5.QtPrintSupport import QPrintDialog, QPrinter, QPrintPreviewDialog, QPrinterInfo
from PyQt5.QtWebKitWidgets import QWebPage, QWebView
from PyQt5.QtWebKit import QWebSettings

app1 = QApplication(sys.argv)

web = QWebView()

style_url1 = 'file:///home/umbrella/PycharmProjects/zp/bootstrap_mod/example/bootstrap.css'
web.settings().setUserStyleSheetUrl(QUrl(style_url1))
style_url2 = 'file:///home/umbrella/PycharmProjects/zp/bootstrap_mod/example/application.css'
web.settings().setUserStyleSheetUrl(QUrl(style_url2))
style_url3 = 'file:///home/umbrella/PycharmProjects/zp/bootstrap_mod/example/discovery.449c10a436c997c3eee5afd5021da3a2.css'
web.settings().setUserStyleSheetUrl(QUrl(style_url3))
style_url4 = 'file:///home/umbrella/PycharmProjects/zp/bootstrap_mod/example/docs.min.css'
web.settings().setUserStyleSheetUrl(QUrl(style_url4))
style_url5 = 'file:///home/umbrella/PycharmProjects/zp/bootstrap_mod/example/lounge.f668c82e65f78693a6a62a5c7d3e54b8.css'
web.settings().setUserStyleSheetUrl(QUrl(style_url5))




web.load(QUrl('file:///home/umbrella/PycharmProjects/zp/bootstrap_mod/example.html'))


#web.setStyleSheet("qrc:/bootstrap_mod/example/bootstrap.min.css")
#view.settings().setUserStyleSheetUrl(QUrl.fromLocalFile("style.css"))



#web.settings().
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