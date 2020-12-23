# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 16:03:44 2020

@author: loris


Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre 
a soma dos quadrados dos elementos do vetor.


"""
numeros = [] 
quadrados = [] 

for n in range(0,10):
    ent = int(input("Digite um numero: "))
    numeros.append(ent)
    
for n in range(0, 10):
    quadr = numeros[n] * numeros[n]
    quadrados.append(quadr)
print(numeros)
print(quadrados)
print(sum(quadrados))