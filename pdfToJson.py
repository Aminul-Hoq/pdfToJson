from pdfminer.pdfpage import PDFPage
import textToDictionary
import argparse
import json
import os
from PyPDF2 import PdfFileReader

list = []
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", required=True,
                help="path to input directory of pdf")
args = vars(ap.parse_args())


def pdfParser(args):
    fp = open(str((args["file"])))
    pdf = PdfFileReader(fp)
    # Create a PDF interpreter object.
    # Process each page contained in the document.
    create_file = open("export.json", "a")
    for page in PDFPage.get_pages(fp):
        page_data = textToDictionary.converter(page, counter)
        if len(page_data) != 0:
            list.append(page_data)

    json_data = json.dumps(list, indent=2)
    create_file.write(json_data)
    # print(list)


if __name__ == '__main__':
    pdfParser(args)
