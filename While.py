# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 20:31:21 2020

@author: danny
"""
import time as time

'''
x = input("Ingrese un valor: ")
x = int(x)
y = 1

while y <= x:
    print(y)
    y = y + 1
    time.sleep(0.1)

y = 1

while True:
    print(y)
    y = y + 1
    time.sleep(0.1)
    if y >= x:
        break
'''

while True:
    x = input("Ingrese un numero: ")
    
    if x == 'q' or x == 'quit':
        break
    
    x = int(x)
    y = 1
    
    while True:
        print(y)
        y = y + 1
        time.sleep(0.1)
        if y >= x:
            break