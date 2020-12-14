from random import randint
import re
from docx import Document
import os

path = r"js01.docx"
document = Document(path)
kk = 0
isp = 0
# q = []
mq = []
# a = []
ra = []
s = ""
miniment = 0
duoxuan = 0


def panduanti():
    global s, ra, mq
    if "√" in s:
        s = "（判断题 T or F）" + s
        ra.append("T")
        s = s.replace("√", "")
        mq.append(s)
        s = ""

    elif "×" in s or "╳" in s or "X" in s:
        s = "（判断题 T or F）" + s
        ra.append("F")
        s = s.replace("×", "")
        s = s.replace("╳", "")
        s = s.replace("X", "")
        mq.append(s)
        s = ""


for paragraph in document.paragraphs:
    j = 4
    # print(paragraph.text)
    if "1、" in paragraph.text or kk > 0:
        kk += 1
        spr = paragraph.text
        s += spr + "\n"
        if re.search("[0-9]*", spr).group(0) is not "":
            s = spr + "\n"
            isp = 0

        if re.search("[0-9]、", s) is not None or re.search("[0-9].", s) is not None:
            if "√" in s or "×" in s or "╳" in s or "X" in s:
                panduanti()
                continue

            rrra = re.search("[A-Z]*[A-Z]", s)
            if rrra is not None:
                miniment = len(rrra.group(0))
                if miniment > 1 and duoxuan == 0:
                    s = "（多选）" + s
                    duoxuan = 1
            else:
                continue

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
                duoxuan = 0
                isp = 0

# for i in mq:
#     print(i)
#     print("@\n")

isansmq = [0 for i in range(len(mq))]

mode = int(input("1.you choose the question's index\n"
                 "2.auto random question's index\n"
                 "3.one by one test from x to end\n"))
op = 0
ansIndex = 0
rightIndex = 0
i = 0
index = 0
if mode == 3:
    index = int(input(f"input x(1-{{indexx}}):".format(indexx=len(mq))))
    if index < 1 or index > len(mq):
        print("{indexx} in illegal".format(indexx=index))

# print(len(mq))
while 1:
    if mode == 1:
        i = int(input("question(1 - {kk}):".format(kk=len(mq))))
    elif mode == 2:
        i = randint(1, len(mq))
        # print("i:", end="")
        # print(i)
        if ansIndex >= len(mq):
            break
        if isansmq[i-1] == 1:
            continue
        else:
            isansmq[i-1] = 1
    elif mode == 3:
        i = index
        index += 1
    else:
        print("Unknown")
        break
    i -= 1
    if i < 0 or i >= len(mq):
        break
    print("第{ii}题".format(ii=i+1))
    print(mq[i])
    ans = input("answer(input 'quit' to quit):")
    if ans == "quit":
        break
    if ans.upper() == ra[i]:
        print("right!!")
        rightIndex += 1
    else:
        print("wrong")
    ansIndex += 1
    op = int(float(rightIndex / ansIndex) * 10000 + 0.5) / 100
    print("正确答案：" + ra[i])
    print("正确率：{x}%  {rights}/{anss}".format(x=op,anss=ansIndex,rights=rightIndex))
    print()
os.system("pause")
