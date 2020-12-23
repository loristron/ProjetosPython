# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 12:19:15 2020

@author: loris

Faça um programa que mostre os n termos da Série a seguir:
  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
Imprima no final a soma da série.

"""
s = 0
d = 1

ene = int(input("Digite um valor de n: "))

for n in range (1, ene+1):
    s += n / d
    d +=2

print(round(s, 2))