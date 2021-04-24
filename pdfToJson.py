from pdfminer.pdfpage import PDFPage
import textToDictionary
import argparse
import json
import os
from PyPDF2 import PdfFileReader

List = []
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", required=True,
                help="path to input directory of pdf")
args = vars(ap.parse_args())


def pdfParser(args):
    path = (args["file"]) or (args["f"])
    print("[Opening pdf file for processing....]")
    fp = open(path, 'rb')
    pdf = PdfFileReader(fp).getDocumentInfo()
    List.append({"title": pdf.title,
                 "creator": pdf.creator,
                 "proucer": pdf.producer,
                 })
    print("[Reading Text by page from file....]")
    count = 1
    page_data = ''
    for page in PDFPage.get_pages(fp):
        print("[Processing Page " + str(count) + ".....]")
        page_data += textToDictionary.converter(page)
        count += 1
    data = textToDictionary.groupData(page_data)
    if len(data) != 0:
        List.append(data)
    print("[Exporting JSON file....]")
    json_data = json.dumps(List, indent=2)
    create_file = open("export.json", "w")
    create_file.write(json_data)


if __name__ == '__main__':
    pdfParser(args)
