# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 13:12:57 2020

@author: loris

Faça um programa que receba dois números inteiros e gere os números 
inteiros que estão no intervalo compreendido por eles.


"""

entrada1 = int(input("Digite o primeiro numero: "))
entrada2 = int(input("Digite o segundo numero: "))
lista = []

for n in range(entrada1, entrada2+1):
    lista.append(n)

print(lista)