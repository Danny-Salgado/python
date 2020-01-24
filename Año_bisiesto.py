# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 21:00:41 2020

@author: danny
"""

def añobisiesto(año):
    if año >= 100 and año <= 999:    
        año = año / 10
    
    if año >= 1000:    
        año = año / 100
    
    año = str(año)
    año = año.split('.')
    año = int(año[0])
    año1 = int(año[1])
    
    a = año%4
    c = año%4

    for b in range (0,24):
        if a == b and c == b:
            return True
        else:
            return False

año = int(input("Ingrese el año: "))

print(añobisiesto(año))