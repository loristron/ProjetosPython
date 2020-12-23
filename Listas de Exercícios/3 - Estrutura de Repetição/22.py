# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 16:00:02 2020

@author: loris

Altere o programa de cálculo dos números primos, informando, caso o número não seja primo
por quais número ele é divisível.


"""


entrada = int(input("Digite um numero para saber se é primo: "))
listaDivisores = []
divisores = 0
for n in range(1, entrada+1): 
    if entrada % n == 0:
        divisores += 1
        listaDivisores.append(n)
if divisores > 2:
    print("O numero não é primo!\nSeus divisores são: "+str(listaDivisores))
if divisores <= 2:
    print("O numero é primo! ")     