# -*- coding: utf-8 -*-
"""
初めてのpythonレッスン22

オブジェクトの作成(変数と関数をまとめたもの)
クラス：オブジェクトの設計図
インスタンス；クラスを実体化したもの

Created on Tue Jun  7 21:01:16 2016

@author: B5_2
"""

class User(object):
    def __init__(self, name):#インスタンスの初期化
        self.name = name
    def greet(self):#クラス内の関数
        print ("my name is %s! " % self.name)
        
bob = User("Bob")
tom = User("Tom")
print (bob.name)
bob.greet()
tom.greet()