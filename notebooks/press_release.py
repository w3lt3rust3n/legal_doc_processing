#!/usr/bin/env python
# coding: utf-8

# ## 1 - Impots
# --------------------


# import legal_doc_processing as ldp
# from legal_doc_processing.information_extraction import *
# from legal_doc_processing.segmentation import *
# from legal_doc_processing.utils import *


from notebooks.packages import *
from notebooks.paths import *

# path and fn


def get_defendant(raw_text):
    """extract defendant """

    # extract lines with 'against'
    lines = [
        i.replace("\u200b", "").replace("\t", " ") for i in raw_text.splitlines() if i
    ]
    cands = [i for i in lines[:300] if "against" in i.lower()]

    # sep pred
    preds = [
        k.lower()
        .split("against")[1]
        .split("for")[0]
        .replace("defendant", "")
        .replace("defendants", "")
        .strip()
        .capitalize()
        for k in cands
        if len(k) > 5
    ]

    if preds:
        return preds[0]

    return "-- None --"


# file_path
file_path_list = x_data_files(20, "press")

# read file
raw_text_list = [load_data(file_path) for file_path in file_path_list]
raw_text_list[0]

# clean and first
clean_pages_list = [clean_doc(raw_text) for raw_text in raw_text_list]
first_page_list = [pages[0] for pages in clean_pages_list]
first_page_list[0]


# pred defendant
def_list = [get_defendant(txt) for txt in raw_text_list[0:12]]
def_list


list(zip(file_path_list, def_list))
