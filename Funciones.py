# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 18:23:43 2020

@author: danny
"""

def mensaje():
    print("Enter next value")

print("We start here")
mensaje()
print("The end is here")

def hi(name):
    print("Hi",name)
    
hi("Danny")

a = int(input("Ingrese un valor numérico: "))
b = int(input("Ingrese un valor numérico: "))

def resta(a,b):
    print(a-b)
    
resta(a,b)

def multiplicar(a,b):
    return a * b

w = multiplicar(a,b)

print(w)

def wishes():
    print("My Wishes")
    return "Happy Birthday"

print(wishes())

lista = ["Hola","Danny","Salgado","Angelo"]

def hola(lista):
    for i in lista:
        print("Hola",i)

hola(lista)

def crearlista(a):
    lista1 = []
    for i  in range(a):
        lista1.append(i)
    return lista1

print(crearlista(a))