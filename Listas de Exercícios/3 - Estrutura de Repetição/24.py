# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 16:52:22 2020

@author: loris

Faça um programa que calcule o mostre a média aritmética de N notas.


"""
import statistics as stc 

repete = True
lista = [] 

while repete == True: 
    entrada = input("Digite o valor da nota. Para encerrar, digite e: ")
    if entrada == 'e' or entrada == 'E':
        repete = False
        continue
    numero = int(entrada)
    lista.append(numero)

media = stc.mean(lista)
print(media)
        
