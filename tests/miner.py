from io import StringIO
import pdfRead
import PyPDF2 as pyPdf
# import os
# import tabula
import json
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

output_string = StringIO()


def MinerReader(file):
    with open('../2020-cdp-water-response.pdf', 'rb') as inFile:
        pdf = pyPdf.PdfFileReader(inFile)
        info = pdf.documentInfo
        parser = PDFParser(inFile)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
        output = output_string.getvalue()
        return output, info


def JsonConverter(data):
    # tables = tabula.read_pdf(file, pages="all", multiple_tables=True)
    # json_data = tabula.convert_into_by_batch("./", output_format="json", pages="all")
    # # print(tables)
    # print(json_data)
    data = json.dumps(data)
    formatj = json.loads(data)
    # print(formatj)


if __name__ == '__main__':
    with open('../2020-cdp-water-response.pdf', 'rb') as in_file:
        output, info = MinerReader(in_file)
    JsonConverter(output)
