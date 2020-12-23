# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 16:05:32 2020

@author: loris

Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo 
usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os 
números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões)
executados.


"""

numero = int(input("\nDigite um número: "))
lista = []
divisoes = 0

for i in range(1, numero + 1):
    if numero % i == 0 and i != 1 and i != numero:
        divisoes += 1
    else:
        lista.append(i)
        divisoes += 1
print("Números primos: ", lista)
print("Número de divisões", divisoes)
            