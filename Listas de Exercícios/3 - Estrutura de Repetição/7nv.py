# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 23:24:05 2020

@author: loris

Faça um programa que leia 5 números e informe o maior número.

"""

count  = 0 
lista = []

while count !=5:
    numero = int(input("Digite o numero "+str(count)+" : "))
    lista.append(numero)
    count += 1 

resposta = max(lista)
print("\nO maior numero digitado é "+str(resposta))