# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 15:10:10 2020

@author: loris

Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
Ex.: 5!=5.4.3.2.1=120

"""
print("Cálculo de Fatorial")
entrada = int(input("Insira o numero a ser calculado: "))

fatorial = 1
for n in range(1, entrada + 1):
    fatorial *= n
    
print(str(entrada)+"! = "+str(fatorial))