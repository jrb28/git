# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 14:32:21 2017

@author: jrbrad
"""

x = input('Please enter a number:')

try:
    x = float(x)
except:
    print('The input could not be interpreted as a numerical value')
    
print(x)       # This is a debugging statement

y = x/2

print(y)