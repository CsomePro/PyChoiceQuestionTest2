# PyChoiceQuestionTest 3.0
### 运行环境Python3
参考此文配置Python3环境

[Python3 环境搭建](https://www.runoob.com/python3/python3-install.html)
### 安装python-docx库
配置完Python3环境后

在Windows命令提示符中输入下列代码，由于安装python-docx库
62.htm)

`pip install python-docx`

[安装教程](https://www.jb51.net/article/1738)

### 使用说明
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

version 2  `docxx/main02.py` （推荐）

使用说明：按提示操作

（注意：必须是`.docx`后缀的word文档，`.doc`的不支持）

效果展示：
``` python
Initializing...
Enter your Question bank filename or file path:js01.docx
1.you choose the question's index
2.auto random question's index
3.one by one test from x to end
3
input x(1-100):4
第4题
4、我国《兵役法》规定：预备役人员必须按照规定参加军事训练，随时准备（  ），保卫祖国。
A、执行急难险重任务 B、参军参战 C、建设祖国 D、执行战斗任务

answer(input 'quit' to quit):quit
Do you want to save(y/n)y
```

### 更新功能说明
mian.py version 1

2020.12.13 version 1.0

实现基础的功能

--------------------------

main02.py verison 2

2020.12.14 version 2.0.4

实现时随机题目不重复

修改 模式3中可以从任意位置开始

添加 显示顺序题号

2020.12.15 version 2.1

修改 模式2中随机题目，正答得题目不再随机，回答错误的题会被再次随机到

添加 模式3中可以循环自测从x到end的题目，且出题逻辑模式2一样（不同在于模式3是依次顺序的）

2020.12.16 version 2.2

重大改版

添加 增加用户交互，降低使用难度

添加 保存进度，断点继续

修改 更改题库不再需要修改代码，可按提示操作

2020.12.18 version 2.2.1

添加 在回答问题时用数字1234来替代ABCD，方便输入

添加 显示当前题库
