# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 14:03:33 2020

@author: loris

Faça um programa que peça dois números, base e expoente
 calcule e mostre o primeiro número elevado ao segundo número. 
 Não utilize a função de potência da linguagem.


"""

base = int(input("Insira a base: "))
pot = int(input("Insira a potência: "))


for n in range(1, pot):
    baseFinal = base * base

print(str(base)+" ^ "+str(pot)+" = "+str(baseFinal))
    