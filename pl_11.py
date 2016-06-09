# -*- coding: utf-8 -*-
"""
初めてのpythonレッスン11

セット(集合型) - (重複を許さない)

Created on Tue Jun  7 15:49:26 2016

@author: B5_2
"""

a = set([1, 2, 3, 4, 3, 2]) # 重複を許さない
print(a)

b = set([3,4,5])

print(a - b) #差集合
print(a | b) #和集合
print(a & b) #積集合
print(a ^ b) #どちらかにしかないもの
