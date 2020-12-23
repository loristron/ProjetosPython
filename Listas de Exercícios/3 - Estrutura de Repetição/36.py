# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 21:27:41 2020

@author: loris

Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo 
usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e 
final devem ser informados também pelo usuário, conforme exemplo abaixo:
    
    
Montar a tabuada de: 5
Começar por: 4
Terminar em: 7

Vou montar a tabuada de 5 começando em 4 e terminando em 7:
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35


Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.

"""


print("Tabuada do seu jeito!")

validado = False

while validado == False: 
    tabuada = int(input("Mostrar tabuada de: "))
    comeco = int(input("Começar de: "))
    fim = int(input("Terminar em: "))
    if comeco < fim and comeco != fim:
        validado = True

for n in range(comeco, fim+1):
    print(str(tabuada)+" x "+str(n)+" = "+str(tabuada*n))














