# -*- coding: utf-8 -*-
"""
初めてのpythonレッスン16

for ループ処理

Created on Tue Jun  7 19:57:39 2016

@author: B5_2
"""

sales = [13, 3523, 31, 238]
sum = 0

for sale in sales:#for A in B (Bから順に取り出しAに入れて出力する)
    sum += sale
else:#ループが終わった後に一回だけしてほしい処理
    print (sum)

#continue(一回だけスキップ) break(ループを脱出)
for i in range(10):
    if i == 3:
        continue
    print(i)
    
for i in range(10):
    if i == 3:
        break
    print(i)