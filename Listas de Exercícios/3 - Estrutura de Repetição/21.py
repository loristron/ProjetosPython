# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 15:54:33 2020

@author: loris

Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
Um número primo é aquele que é divisível somente por ele mesmo e por 1.


"""

entrada = int(input("Insira o numero para verificar se é primo: "))

divisores = 1
for n in range(1, entrada):
    if entrada % n == 0:
        divisores += 1
        
if divisores > 2:
    print("Não é primo! ")
if divisores <= 2:
    print("O número é primo!")