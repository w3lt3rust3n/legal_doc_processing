from legal_doc_processing import logger

import re


def give_txt():
    """ """

    fn = "./data/files/cftc/7117-15/press-release.txt"

    with open(fn, "r") as f:
        txt = f.read()

    return txt


def clean_in_line_break(txt: str) -> str:
    """transform 'hello comment\nca va'  en 'hello comment ca va' """

    break_ = "--BREAK--"
    endline_ = "--ENDLINE--"

    lines = txt.splitlines()
    lines = [i.strip() for i in lines]
    txt_1 = "\n".join(lines)

    txt_2 = txt_1.replace(".\n", f".{endline_}\n")
    txt_3 = txt_2.replace("\n\n", f"\n{break_}\n")

    txt_4 = txt_3.replace("\n", " ")
    txt_5 = txt_4.replace(f" {break_} ", break_)
    txt_6 = txt_5.replace(f"{break_}", f"\n\n")
    txt_7 = txt_6.replace(f"{endline_}", f"\n")

    txt_8 = txt_7.replace("\n\n", "\n")

    return txt_8


def clean_very_short_lines(txt: str, threshold: int = 5) -> str:
    """clean lines too short """

    lines = txt.splitlines()
    lines = [i.strip() for i in lines if len(i.strip()) > threshold]
    new_txt = "\n".join(lines)

    return new_txt


def do_strip(txt: str) -> str:
    """ """

    lines = txt.splitlines()
    lines = [i.strip() for i in lines]
    new_txt = "\n".join(lines)

    return new_txt


# def handle_double_break(txt: str, breaker="--BREAK--"):
#     """detect and replace\n\n by sec char"""

#     new_txt = txt.replace("\n\n", breaker)
#     new_txt = txt.replace("\n\n", breaker)

#     new_txt = new_txt.replace(f"{breaker}{breaker}", breaker)
#     new_txt = new_txt.replace(f"{breaker}{breaker}", breaker)

#     new_txt = new_txt.replace(f"\n{breaker}", breaker)
#     new_txt = new_txt.replace(f"\n{breaker}", breaker)

#     new_txt = new_txt.replace(f"{breaker}\n", breaker)
#     new_txt = new_txt.replace(f"{breaker}\n", breaker)

#     new_txt = new_txt.replace(f"{breaker}{breaker}", breaker)
#     new_txt = new_txt.replace(f"{breaker}{breaker}", breaker)

#     new_txt = new_txt.replace(f"{breaker}\n{breaker}", breaker)
#     new_txt = new_txt.replace(f"{breaker}\n{breaker}", breaker)

#     new_txt = new_txt.replace(breaker, f"\n{breaker}\n")

#     return new_txt


def split_intro_article(txt: str) -> str:
    """ """

    splitter = "\nWashington DC"

    idx = txt.lower().find(splitter.lower())
    intro, article = txt[:idx], txt[idx + 1 :]

    return intro, article


def find_id_line_in_intro(txt: str, len_max=35) -> str:
    """ """

    lines = [i for i in txt.splitlines() if len(i) < len_max]
    idx_list = [i for i, j in enumerate(lines) if j.lower().startswith("Release".lower())]
    if len(idx_list) != 1:
        return -1
    return idx_list[0]


def find_date_line_in_intro(txt: str, len_max=35) -> str:
    """ """

    month_list = [
        "janu",
        "febr",
        "marc",
        "apri",
        "may",
        "june",
        "july",
        "augu",
        "septem",
        "octo",
        "novem",
        "decem",
    ]
    lines = [i for i in txt.splitlines() if len(i) < len_max]
    idx_list = list()
    for month in month_list:
        cand_list = [i for i, j in enumerate(lines) if month.lower() in j.lower()]
        idx_list.extend(cand_list)

    if len(idx_list) != 1:
        return -1
    return idx_list[0]


def structure_cftc_press_release(txt):

    dd = {
        "id": "--ERROR--",
        "date": "--ERROR--",
        "h1": "--ERROR--",
        "article": "--ERROR--",
        "end": "--ERROR--",
        "error": 0,
    }

    try:

        # clean double breaks and fake lines
        new_txt_1 = clean_in_line_break(txt)

        # strip
        new_txt_2 = do_strip(new_txt_1)

        # intro article
        intro, article = split_intro_article(new_txt_2)

        # idx id and date
        idx_id_line = find_id_line_in_intro(intro)
        idx_date_line = find_date_line_in_intro(intro)

        # split extract
        intro_lines = intro.splitlines()
        if idx_id_line != -1:
            dd["id"] = intro_lines[idx_id_line]

        if idx_date_line != -1:
            dd["date"] = intro_lines[idx_date_line]

        # h1
        intro_lines[idx_id_line] = ""
        intro_lines[idx_date_line] = ""

        intro_intermediate = "\n".join(intro_lines)
        dd["h1"] = clean_very_short_lines(intro_intermediate)

        # article and end
        split_article = article.split("\n\n")
        dd["article"] = "\n\n".join(split_article[:-2])
        dd["end"] = "\n\n".join(split_article[-2:])
    except Exception as e:
        logger.error(e)
        dd["error"] = e

    return dd