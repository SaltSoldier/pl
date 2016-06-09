# -*- coding: utf-8 -*-
"""
初めてのpythonレッスン15

条件分岐 if

Created on Tue Jun  7 19:50:57 2016

@author: B5_2
"""

score = 45
if score > 60:
    print ("ok!")
elif score > 40:
    print ("soso...")
else:
    print ("ng!")
    
print ("OK!" if score > 60 else "NG!") #特殊な構文