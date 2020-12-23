# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 18:15:53 2020

@author: loris

Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120

"""

entrada = int(input("Insira um numero para cálculo de fatorial: "))

count = entrada
fatorial = 1
for n in range(1, entrada+1):
    fatorial *= n
print(str(entrada)+"! = ", end="")
while count != 0:
    if count == entrada:
        print(" "+str(count)+" ", end="")
    else:
        print(" x "+str(count)+" ", end="")

    count -= 1
print(" = "+str(fatorial))
    
        