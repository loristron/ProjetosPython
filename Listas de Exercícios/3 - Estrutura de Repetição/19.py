# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 15:23:17 2020

@author: loris

Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

"""

listando = True
lista = []

while listando == True:
    entrada =  input("Insira um conjunto de numeros. Digite c para calcular: ")
    if entrada == 'c' or entrada == 'C':
        break
    if int(entrada) < 0 or int(entrada) > 1000:
        print("Entrada não computada. ")
    else: 
        lista.append(int(entrada))

print("A lista digitada foi: "+str(lista))
print("O maior numero é: "+str(max(lista)))
print("O menor número é: "+str(min(lista)))
print("A soma dos números é: "+str(sum(lista)))