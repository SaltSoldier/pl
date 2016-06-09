# -*- coding: utf-8 -*-
"""
初めてのpythonレッスン10

タプル(変更ができない)


Created on Tue Jun  7 15:40:24 2016

@author: B5_2
"""

a = (2,5,8) #変更ができないのは要素の値だけ，よって繰り返しや連結はできる
# len + * []
print (len(a)) # 3
print (a * 3) #繰り返し

# a[2] = 10 などの代入演算はできない

#タプル<>リスト
#リスト　→　タプル
b = list(a)
print (b)
#タプル　→　リスト
c = tuple(b)
print(c)