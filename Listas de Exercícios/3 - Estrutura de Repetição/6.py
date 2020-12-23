# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 23:19:35 2020

@author: loris


Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. 
Depois modifique o programa para que ele mostre os números um ao lado do outro.


"""


print("Um abaixo do outro: ")
for n in range(0,11):
    print(n)
    
    
print("Um ao lado do outro: ")
lista = []
for n in range(0, 11):
    lista.append(n)
print(lista)