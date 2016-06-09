# -*- coding: utf-8 -*-
"""
初めてのpythonレッスン13

文字列にデータを取り組む

Created on Tue Jun  7 19:32:02 2016

@author: B5_2
"""

a = 10
b = 1.234234
c = "taguchi"
d = {"fkoji":200, "dotinstall":500}
print ("age: %d" %a)#整数出力
print ("age: %10d" %a)#10桁で表示(そこまで桁がなければ空欄表示)
print ("age: %010d" %a)#10桁で表示(そこまで桁がない場合は0を表示)
print ("price: %f" %b)#小数出力
print ("price: %.2f" %b)#小数点以下2桁まで表示
print ("name: %s" %c)#文字列出力
print ("sales: %(fkoji)d" % d)#辞書型の出力
print("%d and %f"%(a,b))#複数の値を同時に出力