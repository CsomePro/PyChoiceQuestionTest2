import time
from random import randint
import re
import os
import json

# import尝试段
count = 3
while count:
    try:
        import requests

        count = 3
        break
    except ImportError:
        print('requests模块未安装,现在准备开始安装...')
        os.system("pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple")
        count -= 1
        continue

while count:
    try:
        from docx import Document

        count = 3
        break
    except ImportError:
        print('docx模块未安装,现在准备开始安装...')
        os.system("pip install python-docx -i https://pypi.tuna.tsinghua.edu.cn/simple")
        count -= 1
        continue

while count:
    try:
        import colorama

        count = 3
        break
    except ImportError:
        print('colorama模块未安装,现在准备开始安装...')
        os.system("pip install colorama -i https://pypi.tuna.tsinghua.edu.cn/simple")
        count -= 1
        continue

if count != 3:
    print("加载失败，请稍后再试。")
    os.system("pause")
    exit(-1)

# --------------------------------------------------------------------------------- #
# windows初始设置
colorama.init(autoreset=True)


# --------------------------------------------------------------------------------- #

# 函数段
def deletefile(file, flag):
    if os.path.exists(file):
        if flag == 0:
            os.remove(file)
        elif flag == 1:
            os.rmdir(file)


def update_file(downloadUrl, objectName, targetFile):
    # ErrorCode = 0
    mainFile = objectName + "-master/docxx/" + targetFile
    try:
        import zipfile
        # 下载zip文件
        print('正在下载 {targetFilee} 文件，请不要关闭窗口...'.format(targetFilee=targetFile))
        with open('tmp.zip', 'wb') as f:
            f.write(requests.get(downloadUrl).content)
        # 解压zip文件
        zip_file = zipfile.ZipFile('tmp.zip')
        zip_file.extract(mainFile)
        zip_file.close()

        # 复制文件
        print('正在合并文件，请不要关闭窗口...')
        with open(mainFile, 'rb') as source:
            with open(targetFile, 'wb') as destination:
                destination.write(source.read())

        # 删除文件
        os.remove('tmp.zip')
        os.remove(mainFile)
        os.rmdir(objectName + "-master/docxx")
        os.rmdir(objectName + "-master")
        # print('更新成功！重启程序后生效')

    except:
        # zip_file.close()
        print("{targetFilee} 更新失败，请稍后再试。".format(targetFilee=targetFile))
        os.system("pause")
        deletefile('tmp.zip', 0)
        deletefile(mainFile, 0)
        deletefile(objectName + "-master/doxx", 1)
        deletefile(objectName + "-master", 1)
        os.system("pause")
        exit(-1)


def update_this():
    print("检查更新中...")
    url = 'https://github.com/CsomePro/PyChoiceQuestionTest2/archive/master.zip'
    objectname = 'PyChoiceQuestionTest2'
    targetfile = 'main02.py'
    api = 'https://api.github.com/repos/CsomePro/PyChoiceQuestionTest2'
    allInfo = requests.get(api).json()
    new_time = time.mktime(time.strptime(allInfo['updated_at'], "%Y-%m-%dT%H:%M:%SZ"))
    file_time = os.path.getmtime('main02.py') - 28800
    if new_time > file_time:
        inp3 = input("检测到最新版，是否更新?(y/n)")
        if inp3 == 'y' or inp3 == 'Y':
            update_file(url, objectname, targetfile)
            print('main02.py 更新成功！')
            update_file(url, objectname, "js01.docx")
            print('js01.docx 更新成功！')
            update_file(url, objectname, "js02.docx")
            print('js02.docx 更新成功！')
            print("重启程序后生效")
            return 1
        else:
            return 0
    else:
        print("已是最新版")
        return 0


def strreplace(s, n):
    target = "ABCDEFGHI"
    s = s[:n]
    ss = [0 for iii in range(n)]
    for ki in s:
        try:
            inp = int(ki)
            assert inp != 0
            if inp <= n:
                ss[inp - 1] = 1
        except ValueError:
            ss[target.find(ki.upper())] = 1
        except AssertionError:
            ss[target.find(ki.upper())] = 1
    return ss


def lToStr(lTmp):
    target = "ABCDEFGHI"
    stmp = ""
    for ki in range(len(lTmp)):
        if lTmp[ki] == 1:
            stmp += target[ki]
    return stmp


def charChange(s):
    ss = s.replace("Ａ", "A")
    ss = ss.replace("Ｂ", "B")
    ss = ss.replace("Ｃ", "C")
    ss = ss.replace("Ｄ", "D")
    ss = ss.replace("Ｅ", "E")
    return ss


def charChangePoint(s):
    ss = s.replace("、", "", 1)
    ss = ss.replace(".", "", 1)
    ss = ss.replace("．", "", 1)
    return ss


def ansSplit(ans):
    sAns = "ABCDEFGHIJKLMNOPQ"
    sAnsIndex = 0
    ans = ans[1:]
    ansReturn = []
    jj = 0
    lenAns = len(ans)
    while jj < lenAns:
        if ans[jj] == sAns[sAnsIndex]:
            sAnsIndex += 1
            # print(ans[jj])
            jj += 1
            anss = ""
            while jj < lenAns:
                if ans[jj] == sAns[sAnsIndex]:
                    break
                else:
                    anss += ans[jj]
                    jj += 1
            ansReturn.append(charChangePoint(anss))
            jj -= 1
        jj += 1
    return ansReturn


def rightAnsChange(sRight):
    rightAnsReturn = []
    sAns = "ABCDEFGHIJKLMNOPQ"
    for ss in sRight:
        rightIndex = sAns.find(ss)
        rightAnsReturn.append(rightIndex)
    return rightAnsReturn


def panduanti(sInput):
    global questionMap
    questionMode = 3
    rightAnsP = ""
    question = ""
    if "√" in sInput or "对" in sInput:
        rightAnsP = 'T'
        sInput = sInput.replace("对", " ", 1)
        question = sInput.replace("√", " ", 1)
    elif "×" in sInput or "╳" in sInput or "X" in sInput or "错" in sInput:
        rightAnsP = 'F'
        sInput = sInput.replace("×", " ")
        sInput = sInput.replace("╳", " ")
        sInput = sInput.replace("错", " ")
        question = sInput.replace("X", " ")
    dictionary = {
        'questionMode': questionMode,
        'question': question,
        'rightAns': rightAnsP
    }
    questionMap.append(dictionary)


def swap(A, a, b):
    A[a], A[b] = A[b], A[a]
    return A


def randomChange(ansList, choiceList):
    countTmp = 3
    while countTmp:
        randomIndex1 = randint(0, len(choiceList) - 1)
        randomIndex2 = randint(0, len(choiceList) - 1)
        if randomIndex1 == randomIndex2:
            continue
        swap(ansList, randomIndex1, randomIndex2)
        swap(choiceList, randomIndex1, randomIndex2)
        countTmp -= 1
    return ansList, choiceList


# --------------------------------------------------------------------------------- #


# 正文段
init = 1
path = r"js02.docx"  # need to save
ansIndex = 0  # need to save
rightIndex = 0  # need to save
i = 0  # need to save
index = 0  # need to save
isansmq = []  # need to save
mode = 1  # need to save
x = 1  # need to save
combo = 0  # need to save
version = '2.3.4'  # need to save
randomChoice = True  # need to save

print("PyChoiceQuestionTest2\n"
      "version {versionn} Power by CSOME (github.com/CsomePro)\n"
      "------------------------------------------------------".format(versionn=version))

if not os.path.exists(r'data.json'):
    print("Initializing...")
    while 1:
        path = input("请输入题库名或路径 -- Enter your Question bank filename or file path:")
        if os.path.exists(path):
            break
        else:
            print("'{file}' does not exist, please try again.".format(file=path))
    with open(r'data.json', 'w') as f:
        updateCheck = time.time()
        data = {'version': version, 'path': path, 'init': 1, 'updateCheck': updateCheck}
        f.write(json.dumps(data))

else:
    with open(r'data.json', 'r') as f:
        data = json.loads(f.read())
        path = data['path']
        updateCheck = data['updateCheck']
    # 更新检查
    if time.time() - updateCheck > 86400:
        try:
            update_this()
            updateCheck = time.time()
        except requests.exceptions.ConnectionError or requests.exceptions.ConnectTimeout:
            print("当前无网络，请稍后再试。")

    inp1 = input("Do you want to load your data(y/n):")
    if inp1 == 'y' or inp1 == 'Y':
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
                combo = data['combo']
                randomChoice = data['randomChoice']
        if init == 1:
            print("You have not saved, just start initially.")
    else:
        inp2 = input("Do you want to change Question bank(y/n):")
        if inp2 == 'y' or inp2 == 'Y':
            while 1:
                path = input("请输入题库名或路径 -- Enter your Question bank filename or file path:")
                if os.path.exists(path):
                    break
                else:
                    print("'{file}' does not exist, please try again.".format(file=path))

# ----------------------------------------------------------------------------------------
# 文档识别
document = Document(path)
rawData = []
for paragraph in document.paragraphs:
    rawData.append(charChange(paragraph.text))

questionMap = []
question = ""
choice = []
rightAns = []
changeTmp = 0  # 识别题目0，识别选项1
questionMode = 0
lenn = len(rawData)
ii = 0
while ii < lenn:
    if re.match(r'[0-9]+', rawData[ii]) != None:
        s = rawData[ii]
        # 判断题
        if re.search(r"[X对错]\b", s) != None or "╳" in s or "×" in s or "√" in s:
            panduanti(s)
            ii += 1
            continue

        # 选择题
        rightAnsRe = re.search(r'[A-Z]+?\b', s)
        if rightAnsRe != None:
            rightAns = rightAnsChange(rightAnsRe.group(0))
            if len(rightAns) > 1:
                questionMode = 2
            else:
                questionMode = 1
            span = rightAnsRe.span()
            question = s[:span[0]] + "  " + s[span[1]:]
            changeTmp = 1
            ansRaw = ""
            for j in range(ii + 1, lenn):
                if not (re.match(r'[0-9]+', rawData[j]) != None):
                    ansRaw += rawData[j]
                else:
                    ansRawRe = re.split(r'([A-F])', ansRaw)
                    choice = ansSplit(ansRawRe)
                    rightAnsMap = [0 for i in range(len(choice))]
                    for kk in rightAns:
                        rightAnsMap[kk] = 1
                    dictionary = {
                        'questionMode': questionMode,
                        'question': question,
                        'rightAns': rightAnsMap,
                        'choice': choice
                    }
                    questionMap.append(dictionary)
                    ii = j - 1
                    break
    ii += 1

# for i in questionMap:
#     print(i)
#     print("@\n")
print()
if init == 1:
    isansmq = [0 for i in range(len(questionMap))]  # need to save
    print("1.主动选择题目序号 -- you choose the question's index\n"
          "2.自动随机题目序号 -- auto random question's index\n"
          "3.自动顺序（从 x 开始）题目序号 -- one by one test from x to end")
    while 1:
        try:
            mode = int(input("mode:"))  # need to save
            break
        except ValueError:
            print("your input is not INT, please try again")
            continue

    while mode == 3:
        while 1:
            try:
                index = int(input("input x(1-{indexx}):".format(indexx=len(questionMap))))
                break
            except ValueError:
                print("your input is not INT, please try again")
                continue

        x = index
        if index < 1 or index > len(questionMap):
            print("{indexx} in illegal".format(indexx=index))
            continue
        else:
            break
    while 1:
        inp3 = input("是否开启随机选项顺序？(y/n)")
        if inp3 == 'y' or inp3 == 'Y':
            randomChoice = True
            break
        elif inp3 == 'n' or inp3 == 'N':
            randomChoice = False
            break
        else:
            print("please choose y(Yes) or n(No)")
            continue

save = 1  # 判断是否是非法跳出0，或是刷题结束2
tl = ["（单选题）", "（多选题）", "（判断题 T or F）"]
sAns = "ABCDEFGHIJKLMNOPQ"

while 1:
    if mode == 1:
        while 1:
            try:
                i = int(input("question(1 - {kk}):".format(kk=len(questionMap))))
                break
            except ValueError:
                print("your input is not INT, please try again")
                continue

    elif mode == 2:
        i = randint(1, len(questionMap))
        # print("i:", end="")
        # print(i)
        if 0 not in isansmq:
            save = 2
            break
        if isansmq[i - 1] == 1:
            continue

    elif mode == 3:
        i = index
        index += 1
        index = (index - x) % (len(questionMap) - x + 1) + x
        if 0 not in isansmq[x - 1:]:
            save = 2
            break
        if isansmq[i - 1] == 1:
            continue
    else:
        print("Unknown")
        save = 0
        break

    i -= 1
    if i < 0 or i >= len(questionMap):
        save = 0
        break
    print("第{ii}题  ".format(ii=i + 1), end="")
    print("( 题库: {pathh} ".format(pathh=path), end="")
    if randomChoice:
        print("随机选项顺序: ON )")
    else:
        print("随机选项顺序: OFF )")
    if questionMap[i]['questionMode'] <= 2:
        if randomChoice:
            questionMap[i]['rightAns'], questionMap[i]['choice'] = \
                randomChange(questionMap[i]['rightAns'], questionMap[i]['choice'])

        print(tl[questionMap[i]['questionMode'] - 1], end="")
        print(questionMap[i]['question'])
        choices = questionMap[i]['choice']
        choiceIndex = 0
        for choiceOut in choices:
            print(sAns[choiceIndex] + "、", end="")
            choiceIndex += 1
            print(choiceOut)
        ans = input("answer(input 'q' to quit):")
        if ans == "q":
            break
        ans = strreplace(ans, len(questionMap[i]['choice']))
        if ans == questionMap[i]['rightAns']:
            print("\033[1;32mright!!\033[0m")
            rightIndex += 1
            isansmq[i] = 1
            combo += 1
        else:
            print("\033[1;31mwrong!\033[0m")
            combo = 0
        print("正确答案：" + lToStr(questionMap[i]['rightAns']))

    elif questionMap[i]['questionMode'] == 3:
        print(tl[questionMap[i]['questionMode'] - 1], end="")
        print(questionMap[i]['question'])
        ans = input("answer(input 'q' to quit):")
        if ans == "q":
            break
        if ans.upper() == questionMap[i]['rightAns']:
            print("\033[1;32mright!!\033[0m")
            rightIndex += 1
            isansmq[i] = 1
            combo += 1
        else:
            print("\033[1;31mwrong!\033[0m")
            combo = 0
        print("正确答案：" + questionMap[i]['rightAns'])

    ansIndex += 1
    tmp = int(float(rightIndex / ansIndex) * 10000 + 0.5) / 100
    print("正确率：{x}%  {rights}/{anss} ".format(x=tmp, anss=ansIndex, rights=rightIndex))
    if combo != 0:
        print("\033[1;33m{combo} Combo !!\033[0m".format(combo=combo))
    print()

if save == 1:  # 用户选择保存
    if input("Do you want to save(y/n)") == 'y':
        with open(r'data.json', 'w') as f:
            data = {'version': version,
                    'init': 0,
                    'path': path,
                    'ansIndex': ansIndex,
                    'rightIndex': rightIndex,
                    'i': i,
                    'index': i + 1,
                    'mode': mode,
                    'x': x,
                    'combo': combo,
                    'updateCheck': updateCheck,
                    'randomChoice': randomChoice,
                    'isansmq': isansmq}
            f.write(json.dumps(data))
else:
    if save == 2:  # 刷题结束时
        print("题库已刷完！ ", end="")
        tmp = int(float(rightIndex / ansIndex) * 10000 + 0.5) / 100
        print("正确率：{x}%  {rights}/{anss} ".format(x=tmp, anss=ansIndex, rights=rightIndex))
        with open("Report.txt", 'a') as f:  # 保存记录
            report = "\n"
            report += str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + "   mode {modee}\n".format(modee=mode)
            report += "( 题库: {pathh}  ".format(pathh=path)
            if randomChoice:
                report += "随机选项顺序: ON ) "
            else:
                report += "随机选项顺序:OFF ) "
            report += "正确率：{x}%  {rights}/{anss}  ".format(x=tmp, anss=ansIndex, rights=rightIndex)
            report += "\n"
            f.write(report)

    with open(r'data.json', 'w') as f:
        data = {'version': version, 'path': path, 'init': 1, 'updateCheck': updateCheck}
        f.write(json.dumps(data))

os.system("pause")
'''
Hi，这里是CSOME，很高兴你能下载我的项目
这个项目是我第一个公开的开源项目，有不足之处请谅解
有BUG也请及时在Github上反馈
再次感谢你的下载！！！！
'''

