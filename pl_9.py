# -*- coding: utf-8 -*-
"""
初めてのpythonレッスン9

リスト

Created on Tue Jun  7 15:29:15 2016

@author: B5_2
"""

sales = [50, 100, 80, 45]
# sort / reverse
sales.reverse() #要素を逆順にする
print(sales)
sales.sort() #昇順ソート
print(sales)
sales.sort() #sort&reverseで降順
sales.reverse()
print(sales)

#文字列とリストの相互変換
#文字列　→　リスト
d = "2013/12/15"
print (d.split("/")) #splitはどの文字で区切るか
#リスト　→　文字列
a = ["a" ,"b" ,"c"]
print ("-".join(a)) #どの文字でつなげるか