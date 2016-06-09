# -*- coding: utf-8 -*-
"""
初めてのpython24

モジュール

Created on Tue Jun  7 21:21:21 2016

@author: B5_2
"""
import math, random #モジュールの呼び出し　ヘッダファイルインクルードみたいなもの
from datetime import  date

print (math.ceil(5.2)) #6 小数点以下切り上げ

for i in range(5):
    print (random.random()) #ランダム変数に関するモジュール
    
print (date.today()) # 日付に関するモジュール