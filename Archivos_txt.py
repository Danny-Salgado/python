# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 20:55:46 2020

@author: danny
"""

lista = []

file = open("devices.txt","r")
for i in file:
    #print(i)
    a = 1
file.close()

file = open("devices.txt","r")
for i in file:
    i = i.strip()
    #print(i)
file.close()

file = open("devices.txt","r")
for i in file:
    i = i.strip()
    lista.append(i)
    #print(i)
print(lista)
file.close()