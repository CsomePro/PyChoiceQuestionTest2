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
主代码位于`docxx/main.py`

用法：将mian.py中的 path的值 改为你目标题库的路径

（注意：必须是`.docx`后缀的word文档，`.doc`的不支持）

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
2020.12.13

mian.py 1.0.0

实现基础的功能

--------------------------

2020.12.14

main02.py 2.0.0

实现时随机题目不重复
