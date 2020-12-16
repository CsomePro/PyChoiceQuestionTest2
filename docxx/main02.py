from random import randint
from docx import Document
import re
import os
import json

init = 1
path = r"js02.docx"  # need to save
ansIndex = 0  # need to save
rightIndex = 0  # need to save
i = 0  # need to save
index = 0  # need to save
isansmq = []  # need to save
mode = 1  # need to save
x = 1  # need to save

print("PyChoiceQuestionTest2\n"
      "version 2.2  Power by CSOME\n"
      "-------------------------------------")

if not os.path.exists(r'data.json'):
    print("Initializing...")
    while 1:
        path = input("Enter your Question bank filename or file path:")
        if os.path.exists(path):
            break
        else:
            print("'{file}' does not exist, please try again.".format(file=path))
    with open(r'data.json', 'w') as f:
        data = {'path': path, 'init': 1}
        f.write(json.dumps(data))

else:
    inp1 = input("Do you want to load your data(y/n):")
    with open(r'data.json', 'r') as f:
        data = json.loads(f.read())
        path = data['path']
    if inp1 is 'y' or inp1 is 'Y':
        with open(r'data.json', 'r') as f:
            data = json.loads(f.read())
            init = data['init']
            if init == 0:
                ansIndex = data['ansIndex']
                rightIndex = data['rightIndex']
                i = data['i']
                index = data['index']
                isansmq = data['isansmq']
                mode = data['mode']
                x = data['x']
        if init == 1:
            print("You have not saved, just start initially.")
    else:
        inp2 = input("Do you want to change Question bank(y/n):")
        if inp2 is 'y' or inp2 is 'Y':
            while 1:
                path = input("Enter your Question bank filename or file path:")
                if os.path.exists(path):
                    break
                else:
                    print("'{file}' does not exist, please try again.".format(file=path))

document = Document(path)
kk = 0
isp = 0
mq = []
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
if init == 1:
    isansmq = [0 for i in range(len(mq))]  # need to save
    mode = int(input("1.you choose the question's index\n"
                     "2.auto random question's index\n"
                     "3.one by one test from x to end\n"))  # need to save
    while mode == 3:
        index = int(input(f"input x(1-{{indexx}}):".format(indexx=len(mq))))
        x = index
        if index < 1 or index > len(mq):
            print("{indexx} in illegal".format(indexx=index))
            continue
        else:
            break

# print(len(mq))
save = 1  # 判断是否是非法跳出，或是刷题结束

while 1:
    if mode == 1:
        i = int(input("question(1 - {kk}):".format(kk=len(mq))))

    elif mode == 2:
        i = randint(1, len(mq))
        # print("i:", end="")
        # print(i)
        if 0 not in isansmq:
            save = 0
            break
        if isansmq[i - 1] == 1:
            continue
        # print(isansmq)

    elif mode == 3:
        i = index
        index += 1
        index = (index - x) % (len(mq) - x + 1) + x
        if 0 not in isansmq[x - 1:]:
            save = 0
            break
        if isansmq[i - 1] == 1:
            continue
        # print(isansmq)
    else:
        print("Unknown")
        save = 0
        break

    i -= 1
    if i < 0 or i >= len(mq):
        save = 0
        break
    print("第{ii}题".format(ii=i + 1))
    print(mq[i])
    ans = input("answer(input 'quit' to quit):")
    if ans == "quit":
        break
    if ans.upper() == ra[i]:
        print("right!!")
        rightIndex += 1
        isansmq[i] = 1
    else:
        print("wrong")
    ansIndex += 1
    tmp = int(float(rightIndex / ansIndex) * 10000 + 0.5) / 100
    print("正确答案：" + ra[i])
    print("正确率：{x}%  {rights}/{anss}".format(x=tmp, anss=ansIndex, rights=rightIndex))
    print()

if save == 1:
    if input("Do you want to save(y/n)") is 'y':
        with open(r'data.json', 'w') as f:
            data = {'init': 0,
                    'path': path,
                    'ansIndex': ansIndex,
                    'rightIndex': rightIndex,
                    'i': i,
                    'index': i+1,
                    'isansmq': isansmq,
                    'mode': mode,
                    'x': x}
            f.write(json.dumps(data))
else:
    with open(r'data.json', 'w') as f:
        data = {'path': path, 'init': 1}
        f.write(json.dumps(data))

os.system("pause")
