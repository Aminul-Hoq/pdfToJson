from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
import io

import re


def converter(page):
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    interpreter.process_page(page)
    data = retstr.getvalue()
    return groupData(data)


def groupData(data):
    group = {}
    pattern2 = "W\d\.\d|W\d\.\d\w|W...\d\.\d\w"
    group_key = (re.findall(pattern2, data))
    split = data.split("\n\n")
    for key in group_key:
        group_by_key = {}
        value = ""
        txt = ""
        for s in split:
            if "(" + key + ")" in s:
                txt = s
                continue
            else:
                value += s
            group_by_key["text"] = txt
            group_by_key["value"] = value
        group[key] = group_by_key
    return group
