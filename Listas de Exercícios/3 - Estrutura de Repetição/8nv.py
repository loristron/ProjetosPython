# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 13:05:22 2020

@author: loris

Faça um programa que leia 5 números e informe a soma e a média dos números.


"""

count = 0 
lista = []

while count != 5:
    numero = int(input("Insira um numero: "))
    lista.append(numero)
    count += 1 

soma = sum(lista)
media = soma / len(lista)

print("O tamanho da lista é: "+str(len(lista)))
print("A soma dos números é: "+str(soma))
print("A média dos números é: "+str(media)) 