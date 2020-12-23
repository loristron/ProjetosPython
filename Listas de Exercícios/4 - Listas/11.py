# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 16:48:37 2020

@author: loris

Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.


"""


a = [1,1,1,1,1,1,1,1,1,1]
b = [0,0,0,0,0,0,0,0,0,0]
c = ['a', 'a', 'a', 'a', 'a','a','a','a','a','a']

mescla = []

for n in range(0, 10):
    mescla.append(a[n])
    mescla.append(b[n])
    mescla.append(c[n].upper())

print(a)
print(b)
print(c)
print(mescla)