# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 11:37:00 2020

@author: loris

Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos
seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. 
A entrada de dados deverá terminar quando for lido um número negativo. 

"""


listaEntradas = []

entrada = 0
primIntervalo = 0
segIntervalo = 0
terIntervalo = 0
quarIntervalo = 0


print("Digite um numero negativo para sair. ")

while entrada >= 0:
    entrada = int(input("Digite e verificarei quantos estão nos intervalos: "))
    if entrada >= 0:
        listaEntradas.append(entrada)
    else:
        continue

for n in range(0, len(listaEntradas)):
    if listaEntradas[n] >= 0 and listaEntradas[n] <= 25:
        primIntervalo += 1
    if listaEntradas[n] >= 26 and listaEntradas[n] <= 50:
        segIntervalo += 1
    if listaEntradas[n] >= 51 and listaEntradas[n] <= 75:
        terIntervalo += 1
    if listaEntradas[n] >= 76 and listaEntradas[n] <= 100:
        quarIntervalo += 1 
        

print("\nForam registrados "+str(primIntervalo)+" entre [0-25]")
print("Foram registrados "+str(segIntervalo)+" entre [26-50]")
print("Foram registrados "+str(terIntervalo)+" entre [51-75]")
print("Foram registrados "+str(quarIntervalo)+" entre [76-100]")