# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 14:31:23 2020

@author: loris


A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... 
Faça um programa que gere a série até que o valor seja maior que 500.

"""

t1 = 1
t2 = 0 
t3 = 0

lista = []

while t3 < 233:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    lista.append(t3)

del(lista[len(lista)-1])
print(lista)
