# -*- coding: utf-8 -*-
"""
初めてのpython20

変数のスコープ
pass

Created on Tue Jun  7 20:35:31 2016

@author: B5_2
"""

name = "taguchi"

def hello():#関数内の変数は関数内でしか使われない
    name = "fkoji"
    
hello()
print (name)

#pass(なにも処理しない)
def hello2():
    pass
