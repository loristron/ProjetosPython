# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 15:16:18 2020

@author: loris

Faça um programa que, dado um conjunto de N números, determine o menor valor, 
o maior valor e a soma dos valores.

"""

listando = True
lista = []

while listando == True:
    entrada = input("Insira o conjunto de numeros. Digite 'n' para avançar ")
    if entrada == 'n':
        break
    lista.append(int(entrada))

print("A lista digitada é: "+str(lista))
print("O menor valor da lista é: "+str(min(lista)))
print("O mair valor da lista é: "+str(max(lista)))
print("A soma de todos os valores é de: "+str(sum(lista)))
