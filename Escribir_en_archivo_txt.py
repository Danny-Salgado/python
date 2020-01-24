# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 21:03:21 2020

@author: danny
"""

file = open("devices.txt","a") #a es para escribir

while True:
    newItem = input("Ingrese un valor: ")
    if newItem == 'exit':
        print("All Done")
        break
    
    file.write(newItem+"\n")

file.close()