#coding: utf8

from markdown import markdown
import pdfkit

input_filename = 'bootstrap_mod/example.html'

output_filename = 'README.pdf'

with open(input_filename, 'r') as f:
    html_text = markdown(f.read(), output_format='html4')

options = {
    'page-size': 'Letter',
    'margin-top': '0.25in',
    'margin-right': '0.25in',
    'margin-bottom': '0.25in',
    'margin-left': '0.25in',
    'encoding': "UTF-8",
    'no-outline': None
}


css = ['bootstrap_mod/example/bootstrap.min.css', 'bootstrap_mod/example/application.css',
       'bootstrap_mod/example/discovery.449c10a436c997c3eee5afd5021da3a2.css','bootstrap_mod/example/docs.min.css',
       'bootstrap_mod/example/lounge.f668c82e65f78693a6a62a5c7d3e54b8.css',]

pdfkit.from_string(html_text, output_filename, options=options, css=css)
