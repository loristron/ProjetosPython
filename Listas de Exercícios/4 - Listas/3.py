# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 13:33:41 2020

@author: loris

Faça um Programa que leia 4 notas, mostre as notas e a média na tela.


"""

import statistics as stc 

notas = []

for n in range(0, 4):
    ent = int(input("Nota "+str(n+1)+": "))
    notas.append(ent)

print(notas)
media = stc.mean(notas)
print("Média: "+str(round(media, 2)))
