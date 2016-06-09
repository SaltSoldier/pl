# -*- coding: utf-8 -*-
"""
初めてのpythonレッスン12

辞書型 key value


Created on Tue Jun  7 19:22:37 2016

@author: B5_2
"""

sales = {"taguchi":200, "fkoji":300, "dotinstall":500} #ここで定義した順番で必ずしも出力されるわけではない
print (sales)

print (sales["taguchi"])
sales["fkoji"] = 800
print(sales)

# in 存在するかどうかTrue or Falseで返ってくる
print ("taguchi" in sales) # True

# keys(キー), values(値), items(両方)
print(sales.keys())
print(sales.values())
print(sales.items())