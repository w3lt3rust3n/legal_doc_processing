import re
text="Alex va\n de mieux en \nmieux"
p=re.compile("[^.*?\n.]")
''.join(p.findall(text))