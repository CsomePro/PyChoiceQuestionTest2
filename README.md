# PyChoiceQuestionTest 2

### 下载

version 2.3

直接下载zip  [点击下载](https://github.com/CsomePro/PyChoiceQuestionTest2/archive/master.zip)

仅需配配置Python3运行环境即可

version 2.2.2

Windows不需配置Python3环境，直接下载release版本即可，解压后双击打开即可

非Windows直接下载完整ZIP（Linux自带Python，MacOS需要配置Python环境），双击`main02.py`即可使用

### 运行环境Python3

Windows不需配置Python3环境，直接下载release版本即可

参考此文配置Python3环境

[Python3 环境搭建](https://www.runoob.com/python3/python3-install.html)

### 安装python-docx库（main02.py可自动安装）

配置完Python3环境后

在Windows命令提示符中输入下列代码，由于安装python-docx库
62.htm)

`pip install python-docx`

### 使用说明

version 2  `docxx/main02.py` （推荐）

使用说明：直接双击打开,按提示操作

（注意：必须是`.docx`后缀的word文档，`.doc`的不支持）

效果展示：
``` python
Do you want to load your data(y/n):n
Do you want to change Question bank(y/n):y
Enter your Question bank filename or file path:js01.docx

1.you choose the question's index
2.auto random question's index
3.one by one test from x to end
mode:3
input x(1-100):1
是否开启随机选项顺序？(y/n)y
第1题  ( 题库: js01.docx 随机选项顺序: ON )
（单选题）1、 人们解放军的军衔上出现两杠三星的是（    ）。
A、大校
B、上尉 
C、上校 
D、上将 
answer(input 'q' to quit):3
right!!
正确答案：C
正确率：100.0%  1/1 
1 Combo !!
```

version 1  `docxx/main01.py` （不推荐）

用法：将mian.py中的 path的值 改为你目标题库的路径

(用记事本修改)

`path = r"你的路径"`

修改之后直接双击打开

效果展示
``` python
1.you choose the question's index # 自主选题，自测
2.auto random question's index # 自动随机选题自测
3.one by one test from 1 to end # 按顺序从1开始自测
2
（多选）24、清王朝与法国签订的条约有（）
A.《马关条约》B.《中法新约》C.《北京条约》D.《辛丑条约》

answer:abc
wrong
正确答案：BC
正确率：0.0%  0/1
```

### 更新功能说明
mian.py version 1

2020.12.13 version 1.0

实现基础的功能

--------------------------

main02.py verison 2

2020.12.14 version 2.0.4 ---

实现时随机题目不重复

修改 模式3中可以从任意位置开始

添加 显示顺序题号

2020.12.15 version 2.1 ---

修改 模式2中随机题目，正答得题目不再随机，回答错误的题会被再次随机到

添加 模式3中可以循环自测从x到end的题目，且出题逻辑模式2一样（不同在于模式3是依次顺序的）

2020.12.16 version 2.2 ---

重大改版

添加 增加用户交互，降低使用难度

添加 保存进度，断点继续

修改 更改题库不再需要修改代码，可按提示操作

2020.12.18 version 2.2.1 ---

添加 在回答问题时用数字1234来替代ABCD，方便输入

添加 显示当前题库

2020.12.20 version 2.2.2 ---


修复 若干BUG，兼容Python3.9

添加 Combo，连续答对有激励

添加 `Report.txt`，每次用模式2或模式3刷题时，刷完一次之后就会保存正确率和时间，记录成长过程

2020.12.23 version 2.3 ---

修复 若干BUG，识别算法更换，题目识别更精确

添加 第三方库自动检查，自动安装，降低使用难度

添加 主动检查更新（每24小时检查更新），及时修复BUG

添加 随机选项顺序的选项，加深记忆

添加 部分字体颜色，答对答错更直观

2020.12.25 version 2.3.1 ---

修复 version 2.3.0更新闪退问题

2020.12.26 version 2.3.2 ---

修复 判断题判题BUG

### 常见问题

1. 更新version 2.3出现闪退现象：将同目录下的`data.json`文件删除即可。

2. version 2.3.0 更新出现闪退：手动下载最新zip文件，覆盖即可
