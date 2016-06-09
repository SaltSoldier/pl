# -*- coding: utf-8 -*-
"""
初めてのpythonレッスン19

関数
引数

Created on Tue Jun  7 20:24:04 2016

@author: B5_2
"""

def hello(name, num = 4):#初期値設定可能(引数を省略した場合初期値を使用)
    print("hello %s! " % name * num)

hello("tom", 2)
hello(num = 2, name = "tom")#引数の順番は指定できる
hello("steve", 3)
hello("ryohei")

def hello_return(name, num = 4):#返り値ありの関数
    return("hello %s! " % name * num)

s = hello_return("tom")
print(s)
