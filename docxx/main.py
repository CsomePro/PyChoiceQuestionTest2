from random import randint
import re
from docx import Document
import os

path = r"js02.docx"
document = Document(path)
kk = 0
isp = 0
q = []
mq = []
# a = []
ra = []
s = ""
miniment = 0
for paragraph in document.paragraphs:
    j = 4
    # print(paragraph.text)
    if "1、" in paragraph.text or kk > 0:
        kk += 1
        spr = paragraph.text
        s += spr + "\n"
        if re.search("[0-9]、", s) is not None:
            rrra = re.search("[A-Z]*[A-Z]", s)
            if rrra is not None:
                miniment = len(rrra.group(0))
                if miniment > 1: s += "（多选）" + "\n"
            else:
                continue
            if re.search("[0-9]、", spr) is not None:
                s = spr + "\n"
                isp = 0
            if "A" in spr:
                isp += 1
            if "B" in spr:
                isp += 1
            if "C" in spr:
                isp += 1
            if "D" in spr:
                isp += 1
            if "E" in spr:
                j = 5
                isp += 1
            if isp >= miniment + j:
                # print(s)
                # print()
                # q.append(s)
                rrra = re.search("[A-Z]*[A-Z]", s)
                if rrra is not None:
                    rra = rrra.group(0)
                    ra.append(rra)
                    mq.append(s.replace(rra, "", 1))
                    # print(mq[-1])
                    # print()
                s = ""
                isp = 0

mode = int(input("1.you choose the question's index\n"
                 "2.auto random question's index\n"
                 "3.one by one test from 1 to end\n"))
op = 0
ansIndex = 0
rightIndex = 0
i = 0
index = 0
while (1):
    if mode == 1:
        i = int(input("question(1- {kk}):".format(kk=len(mq))))
    elif mode == 2:
        i = randint(1, len(mq))
    elif mode == 3:
        index += 1
        i = index
    else:
        print("Unknown")
        break
    i -= 1
    if i < 0 or i >= len(mq):
        break
    print(mq[i])
    ans = input("answer:")
    if ans in "-1":
        break
    if ans.upper() == ra[i]:
        print("right!!")
        rightIndex += 1
    else:
        print("wrong")
    ansIndex += 1
    op = int(float(rightIndex / ansIndex) * 10000 + 0.5) / 100
    print("正确答案：" + ra[i])
    print("正确率：{x}%".format(x=op))
    print()
os.system("pause")
