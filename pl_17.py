# -*- coding: utf-8 -*-
"""
初めてのpythonレッスン17

for ループ(辞書編)

Created on Tue Jun  7 20:07:01 2016

@author: B5_2
"""

users = {"taguchi":200, "fcoji":300, "dotinstall":500}
for key, value in users.items():#item(すべてのキー，値をたどる)
    print("key: %s value: %d" % (key, value))
    
for key in users.keys():
    print("key: %s" % key)

for value in users.values():
    print("value: %d" % value)
