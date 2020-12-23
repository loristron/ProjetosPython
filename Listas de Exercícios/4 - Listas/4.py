# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 13:37:17 2020

@author: loris

Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. 
Imprima as consoantes.

"""
vogais = ['A', 'E','I','O','U']
cons = 0
lista = []
consoantes = [] 

for n in range(0, 10):
    ent = input("Digite um caracter: ")
    lista.append(ent.upper())
for i in range(0,10):
    if lista[i] not in vogais:
        cons += 1
        consoantes.append(lista[i])
print("Você digitou "+str(cons)+" consoantes")
print(consoantes)        