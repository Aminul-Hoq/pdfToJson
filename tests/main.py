# import PyPDF2 as pypdf
#
#
# def findInDict(needle, haystack):
#     for key in haystack.keys():
#         try:
#             value = haystack[key]
#
#         except:
#             continue
#         if key == needle:
#             return value
#         if isinstance(value, dict):
#             x = findInDict(needle, value)
#             if x is not None:
#                 return x
#
#
# pdf_object = open('2020-cdp-water-response.pdf', 'rb')
# pdf = pypdf.PdfFileReader(pdf_object)
# xfa = findInDict('/XFA', pdf.resolvedObjects)
# # xml = xfa[7].getObject().getData()
# print(xfa)
# extract_doc_info.py

from PyPDF2 import PdfFileReader
import PyPDF2
import json


def extract_information(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        read_pdf = PyPDF2.PdfFileReader(pdf_file)
        number_of_pages = read_pdf.getNumPages()
        page = read_pdf.getPage(4)
        page_content = page.extractText()
        data = json.dumps(page_content)
        formatj = json.loads(data)
        print(formatj)

if __name__ == '__main__':
    path = '../2020-cdp-water-response.pdf'
    extract_information(path)
