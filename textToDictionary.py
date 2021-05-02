from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
import formatValue
import io

import re


def converter(page):
    rsrc_mgr = PDFResourceManager()
    ret_str = io.StringIO()
    codec = 'utf-8'
    la_params = LAParams()
    device = TextConverter(rsrc_mgr, ret_str, codec=codec, laparams=la_params)
    interpreter = PDFPageInterpreter(rsrc_mgr, device)

    interpreter.process_page(page)
    data = ret_str.getvalue()
    data = data.replace('\n\n of 58', ' ') \
        .replace('\n\nCDP\n\nPage \n\n', ' ') \
        .replace('\n\nPage \n', ' ') \
        .replace('\n\nCDP', ' ')
    return data


def groupData(data):
    group = {}
    pattern = "W\d\.\d|W\d\.\d\w|W...\d\.\d\w"
    group_key = (re.findall(pattern, data))
    group_key = unique(group_key)
    split = data.split("\n\n")
    for key in group_key:
        group_by_key = {}
        txt, value, split = text_value(key, split, group_key)
        group_by_key['text'] = txt
        txt.replace(txt, '')
        group_by_key['value'] = formatValue.formatValue(value, data)
        group[key] = group_by_key
    return group


def text_value(key, split, group_key):
    txt = ""
    value = ""
    for s in split:
        checked_value = ''
        if "(" + key in s:
            txt += s
            split.remove(s)
        else:
            for k in group_key:
                if "(" + k in value:
                    checked_value = ''
                    break
                else:
                    checked_value = s
            value = value + '. ' + checked_value
            if checked_value != '':
                split.remove(checked_value)
    return txt, value, split


def unique(list1):
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list
