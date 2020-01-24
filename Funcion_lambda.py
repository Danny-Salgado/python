# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 19:59:04 2020

@author: danny
"""

a = int(input("Ingrese un valor numérico: "))
b = int(input("Ingrese un valor numérico: "))

c =  lambda a , b: a + b

print(c(a,b))