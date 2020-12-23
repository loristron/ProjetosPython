# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 13:11:08 2020

@author: loris

Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.


"""
lista = []
for n in range (1, 50):
    if n % 2 != 0:
        print(n)
        lista.append(n)

print(lista)
        