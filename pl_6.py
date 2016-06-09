# -*- coding: utf-8 -*-
"""
初めてのpythonレッスン6

文字列
文字数　len
検索 find
切り出し []


Created on Tue Jun  7 14:47:07 2016

@author: B5_2
"""

s = "abcdefghi"
print (len(s)) #文字列の長さを返す
print (s.find("c")) #存在している場所を返す
print (s.find("x")) #存在しない文字列は-1を返す
print (s[2]) #切り出し
print (s[2:5]) #はじまりと終わり指定(start:end)
print (s[2:]) #後ろ空欄は最後まで
print (s[:5]) #前空欄は最初から
print (s[2:-1]) #-をつけると終端から数える(-1は一番最後の文字)