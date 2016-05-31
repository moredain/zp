import sys

from PyQt5.QtCore import QUrl

from PyQt5.QtWidgets import QApplication

from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtWebKitWidgets import QWebView

app1 = QApplication(sys.argv)

web = QWebView()

#web.load(index.txt)
#web.load(QUrl('file:///home/umbrella/PycharmProjects/zp/bootstrap_mod/index.html'))

#pyDir = os.path.abspath(os.path.dirname(__file__))
#baseUrl = QUrl.fromLocalFile(os.path.join(pyDir, "static/"))
#html = """
#    <html><body>
#    <div>Hello World!</div>
#    <img src="test.png"/>
#    </body></html>
#    """
#view.setHtml(html, baseUrl)


web.load(QUrl ("file:///"+"bootstrap_mod/index.html"))


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