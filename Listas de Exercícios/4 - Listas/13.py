# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 18:07:03 2020

@author: loris

Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. 
Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, 
e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).


"""
import statistics as stc

mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
temp = []
total = 0

for n in range (0, 12):
    ent = int(input("Média do mês "+mes[n]+": "))
    temp.append(ent)

mediaTemp = stc.mean(temp)

print("\nTemperatura média anual: "+str(round(mediaTemp, 2))+"º graus")
print("\nTemperaturas acima da média: ")
for n in range(0, 12):
    if temp[n] > mediaTemp:
        count += 1 
        print(str(n+1)+" - "+mes[n]+": "+str(temp[n])+"º graus")