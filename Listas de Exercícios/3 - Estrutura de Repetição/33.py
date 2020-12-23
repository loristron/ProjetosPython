# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 21:18:46 2020

@author: loris

O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia
 as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas
informadas, bem como a média das temperaturas.

"""


import statistics as stc

lendo = True
lista = []

print("Pressione s para calcular")

while lendo == True:
    entrada = input("Digite uma temperatura: ")
    if entrada == 's' or entrada == 'S':
        lendo = False
        continue
    temp = int(entrada)
    lista.append(temp)

media = stc.mean(lista)

print("A maior temperatura encontrada foi de: "+str(max(lista))+"º graus.")
print("A menor temperatura encontrada foi de: "+str(min(lista))+"º graus")
print("A média das temperaturas foi de: "+str(round(media, 2))+"º graus. ")
