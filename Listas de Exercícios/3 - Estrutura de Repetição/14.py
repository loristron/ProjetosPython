# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 14:08:25 2020

@author: loris


Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de 
números pares e a quantidade de números impares.



"""


contador = 0
lista = [] 

while contador != 10:
    entrada = int(input("Insira um inteiro: "))
    lista.append(entrada)
    contador += 1 

par = 0
impar = 0

for n in lista:
    if n % 2 == 0:
        par += 1
    if n % 2 != 0:
        impar += 1

print(str(par)+ " numeros pares e "+str(impar)+" numeros ímpares. ")
    