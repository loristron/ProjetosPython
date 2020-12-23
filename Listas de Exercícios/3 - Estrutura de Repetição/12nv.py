# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 13:18:41 2020

@author: loris


Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
O usuário deve informar de qual numero ele deseja ver a tabuada. 
A saída deve ser conforme o exemplo abaixo:
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50



"""

entrada = int(input("Digite o numero para ver a tabuada: \n"))

for n in range(1, 11):
    multiply = entrada * n
    print(str(entrada)+" X "+str(n)+" = "+str(multiply))
    


