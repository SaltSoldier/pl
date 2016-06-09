# -*- coding: utf-8 -*-
"""
初めてのpythonレッスン21

リスト　<>　関数 map lambda

Created on Tue Jun  7 20:40:15 2016

@author: B5_2
"""

def double(x):
    return x * x
#map(A,B)Bのリストから取り出したものをAの関数に入れて返す
print(map(double, [2, 5, 8]))

#lambda 無名関数(ちょっとした関数を1文で作成)
print(map(lambda x: x * x,[2, 5, 8]))
print("OK")

print(list(map(double, [2, 5, 8])))
print(list(map(lambda x: x * x,[2, 5, 8])))