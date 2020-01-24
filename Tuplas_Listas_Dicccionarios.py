# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 21:03:58 2020

@author: danny
"""

lista = ["r1",2,"r3",4,"r5",6.7]

#print(type(lista))
#print(len(lista))
#print(lista)

#print(lista[-6])

lista[0] = "Hola"

#print(lista)

del lista[3]

#print(lista)

diccionario = dict()

diccionario = {
        1:"Danny",
        2:lista,
        3:"Salgado",
        4:10,
        5:112.6,
        }

print(diccionario[1])
