# -*- coding: utf-8 -*-
"""
初めてのpythonレッスン8

リスト(配列)

Created on Tue Jun  7 15:05:11 2016

@author: B5_2
"""

sales = [255, 100, 353, 400]
# len + * [] (文字列と同じ処理ができる)
print(sales[2]) #353
sales[2] = 100
print(sales[2]) #100

#in(そのリストに値があるかどうか)
print(100 in sales) #返り値はTrueかFalse

#range
print(range(3,10)) #3~10の出力
print(range(3,10,2)) #3~10の間で2づつ出力
print("OK") #3~10の間で2づつ出力

print(list(range(3,10)))
print(list(range(3,10,2)))