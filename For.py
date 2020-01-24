# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 20:12:08 2020

@author: danny
"""

lista = ["r1","r2","r3","r4","s1","s2","s3"]
lista1 = []


for i in lista:
    if "r" in i:
        print(i)
   
 
for j in lista:
    if "s" in j:
        lista1.append(j) 
        
print(lista1)

result = 0
n = 5

for i in range(1, n+1):
    result += i
    print(result)