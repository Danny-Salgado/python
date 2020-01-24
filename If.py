# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 19:50:37 2020

@author: danny
"""

Nombre = input("Ingrese su nombre: ")
Apellido = input("Ingrese su apellido: ")
Edad = input("Ingrese su edad: ")
Edad = int(Edad)
if Edad <= 15:
    a = "Adolecente"
    
if Edad >= 16 and Edad <= 30:
    a = "Joven"
    
if Edad >= 31 and Edad <= 65:
    a = "Adulto"
    
if Edad >= 66 and Edad <= 100:
    a = "Anciano"
    
print("Hola",Nombre,Apellido,", tu eres",a,"por que tu edad es",Edad)