# -*- coding: utf-8 -*-
"""
初めてのpythonレッスン23

クラスの継承

Created on Tue Jun  7 21:01:16 2016

@author: B5_2
"""

class User(object):
    def __init__(self, name):#インスタンスの初期化
        self.name = name
    def greet(self):#クラス内の関数
        print ("my name is %s! " % self.name)

class SuperUser(User):#クラスの継承
    def shout(self):#クラス内の関数
        print ("%s is SUPER!! " % self.name)
        
bob = User("Bob")
tom = SuperUser("Tom")
print (bob.name)
bob.greet()
tom.greet()
tom.shout()