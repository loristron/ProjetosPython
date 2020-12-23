# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 12:39:29 2020

@author: loris

Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, 
Faça um programa que calcule o valor de H com N termos.


"""

n = int(input("Digite um valor de n: "))
h = 0

for n in range(0, n):
    h += 1/(n+1)
print(round(h,2))