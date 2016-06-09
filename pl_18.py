# -*- coding: utf-8 -*-
"""
初めてのpythonレッスン18

while ループ

Created on Tue Jun  7 20:18:17 2016

@author: B5_2
"""

n = 0
while n < 10:
    if n == 3:
        n += 1
        continue
    print(n)
    n += 1
else:
    print("end")

n = 0
while n < 10:
    if n == 3:
        break
    print(n)
    n += 1
else:
    print("end")