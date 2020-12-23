# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 13:15:07 2020

@author: loris

Altere o programa anterior para mostrar no final a soma dos números.


"""

entrada1 = int(input("Digite o primeiro numero: "))
entrada2 = int(input("Digite o segundo numero: "))
lista = []

for n in range(entrada1, entrada2+1):
    lista.append(n)

soma = sum(lista)

print("\nO intervalo digitado é: "+str(lista))
print("A soma final dos numeros é: "+str(soma))

