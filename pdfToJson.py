from pdfminer.pdfpage import PDFPage
import textToDictionary

import json

list =[]


def pdfParser():

    fp = open("2020-cdp-water-response.pdf", 'rb')

    # Create a PDF interpreter object.
    # Process each page contained in the document.
    counter = 1
    create_file = open("abc.json", "a")
    for page in PDFPage.get_pages(fp):
        page_data = textToDictionary.converter(page, counter)
        if (len(page_data) != 0):
            list.append(page_data)
        counter += 1

    json_data = json.dumps(list, indent=2)
    create_file.write(json_data)
    # print(list)


if __name__ == '__main__':
    pdfParser()