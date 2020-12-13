from random import randint

import docx
import re
from docx import Document

path = r"Your Path"
document = Document(path)
kk = 0
# isp = 0
q = []
mq = []
# a = []
ra = []
s = ""
for paragraph in document.paragraphs:
    if "1、 " in paragraph.text or kk > 0:
        kk += 1
        spr = paragraph.text
        s += spr + "\n"
        if re.search("[0-9]、", s) is not None and "D" in spr:
            q.append(s)
            rrra = re.search("（ [A-Z] ）", s)
            if rrra is not None:
                rra = rrra.group(0)
                ra.append(rra)
                mq.append(s.replace(rra, "（  ）"))
            s = ""

mode = int(input("1.you choose\n2.auto rand\n"))

while(1):
    if mode == 1:
        i = int(input("question(1- {kk}):".format(kk=len(mq))))
    elif mode == 2:
        i = randint(1, len(mq))
        print(i)
    else:
        break
    i -= 1
    if i < 0 or i > len(mq):
        break
    print(mq[i])
    ans = input("answer:")
    if ans in "-1":
        break
    if ans.upper() in ra[i]:
        print("right!!")
    else:
        print("wrong")
    print(ra[i])

