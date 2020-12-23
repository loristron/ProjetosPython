# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 16:25:43 2020

@author: loris

Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos,
cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.


"""
a = [1,1,1,1,1,1,1,1,1,1]
b = [0,0,0,0,0,0,0,0,0,0]

mescla = []

for n in range(0, 10):
    mescla.append(a[n])
    mescla.append(b[n])

print(a)
print(b)
print(mescla)