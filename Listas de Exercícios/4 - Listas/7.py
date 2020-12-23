# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 15:49:52 2020

@author: loris

Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.


"""

import numpy as np

numeros = []

for n in range(0, 5):
    ent = int(input("Digite um numero: "))
    numeros.append(ent)

soma = sum(numeros)
mul = np.prod(numeros)

print("\nA soma dos numeros é: "+str(soma))
print("O produto dos números é: "+str(mul))    