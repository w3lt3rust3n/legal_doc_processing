import re


in_txt = "alex va\nde mieux en mieux"


out_txt = "alex va de mieux en mieux"


p = re.compile("*[a-z]\n[a-z]*")
p.match(in_txt)


re.search(r"*[a-z]\\n[a-z]*", in_txt)
