# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 20:26:26 2020

@author: danny
"""

import numpy as np

a = np.array([1,2,3])
print(a,"\n")

b = np.array([(1,2,3),(4,5,6)])
print(b,"\n")

unos = np.ones((3,4))
print(unos,"\n")

ceros = np.zeros((3,4))
print(ceros,"\n")

aleatorios = np.random.random((2,2))
print(aleatorios,"\n")

vacia = np.empty((3,2))
print(vacia,"\n")

full = np.full((2,2),8)
print(full,"\n")

espacio = np.arange(0,30,5)
print(espacio,"\n")

espacio2 = np.linspace(0,2,5)
print(espacio2,"\n")

identidad = np.identity(4)
print(identidad,"\n")

print(b.ndim) #encontrar la dimension
print(b.dtype) #encontrar el tipo de datos
print(b.size) #encontrar el tamaño
print(b.shape,"\n") #encontrar la forma

c = np.array([(8,9,10),(11,12,13)])
c = c.reshape(3,2) 
print(c,"\n")

print(b[1,2],"\n")

print(a.min()) #minimo
print(a.max()) #maximo
print(a.sum(),"\n") #suma

print(np.sqrt(b)) #raiz cuadrada de cada uno de los elementos
print(np.std(b),"\n") #desviación estandar


