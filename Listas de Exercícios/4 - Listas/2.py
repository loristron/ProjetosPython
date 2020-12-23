# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 13:28:52 2020

@author: loris

Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

"""

numeros = []
for n in range(0, 10):
    num = int(input("Numeros: "))
    numeros.append(num)

print(numeros[::-1])