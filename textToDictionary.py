from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
import io

import re


def converter(page, counter):
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    page_data = {}
    interpreter.process_page(page)
    data = retstr.getvalue()
    return groupData(data)


def groupData(data):
    group = {}
    # pattern1 = "W\d\."
    pattern2 = "W\d\.\d|W\d\.\d\w|W...\d\.\d\w"
    group_key = (re.findall(pattern2, data))
    # if not group_key:
    #     group["value"] = data
    # for key in group_key:
    #     group_with_key = {}
    #     for s in data.split("\n\n"):
    #         # print(s + "\n\n\n\n")
    #         if key in s:
    #             sub_group_key = re.findall(pattern2, s)
    #             for sub_key in sub_group_key:
    #                 group_with_sub_key = {}
    #                 if (sub_key+")" in s):
    #                     group_with_sub_key["text"] = s
    #                 else:
    #                     group_with_sub_key["value"] = s
    #                 group_with_key[sub_key] = group_with_sub_key
    #             group[key] = group_with_key
    #         else:
    #             sub_group_key = re.findall(pattern2, s)
    #             for sub_key in sub_group_key:
    #                 group_with_sub_key = {}
    #                 if (sub_key + ")" in s):
    #                     group_with_sub_key["text"] = s
    #                 else:
    #                     group_with_sub_key["value"] = s
    #                 group_with_key[sub_key] = group_with_sub_key
    #             group[key] = group_with_key
    split = data.split("\n\n")
    for key in group_key:
        group_by_key = {}
        for s in split:
            if "(" + key + ")" in s:
                group_by_key["text"] = s

            # Fixme - need to remove spacial character from string
            else:
                group_by_key["value"] = s
        group[key] = group_by_key
    return group
