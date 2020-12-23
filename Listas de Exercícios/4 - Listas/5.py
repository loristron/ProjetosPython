# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 13:43:55 2020

@author: loris

Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. 
Imprima os três vetores.

"""


valores = []
pares = []
impares = []

for n in range(0,10):
    ent = int(input("Digite um numero: "))
    valores.append(ent)

for n in valores:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print("VALORES: ")
print(valores)
print("PARES: ")
print(pares)
print("ÍMPARES: ")
print(impares)