# json_exporter.py

import json
import os
import PyPDF2

from miner_text_generator import extract_text_by_page


def export_as_json(pdf_path, json_path):
    filename = os.path.splitext(os.path.basename(pdf_path))[0]
    data = {'Filename': filename}
    data['Pages'] = []

    counter = 1
    for page in extract_text_by_page(pdf_path):
        text = page[0:100]
        page = {'Page_{}'.format(counter): text}
        data['Pages'].append(page)
        counter += 1

    with open(json_path, 'w') as fh:
        json.dump(data, fh)


def pdf_to_text(pdf_path):
    filename = os.path.splitext(os.path.basename(pdf_path))[0]
    pdfFileObject = open(r"F:\pdf.pdf", 'rb')

    pdfReader = PyPDF2.PdfFileReader(pdfFileObject)

    print(" No. Of Pages :", pdfReader.numPages)

    pageObject = pdfReader.getPage(0)

    print(pageObject.extractText())

    pdfFileObject.close()


if __name__ == '__main__':
    pdf_path = '../2020-cdp-water-response.pdf'
    json_path = pdf_path.replace(".pdf", ".json")
    export_as_json(pdf_path, json_path)