# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 18:15:12 2020

@author: loris

Faça um programa que simule um lançamento de dados. 
Lance o dado 100 vezes e armazene os resultados em um vetor . 
Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma 
função para gerar numeros aleatórios, simulando os lançamentos dos dados.


"""
from random import randint 

print("SIMULADOR DE LANÇAMENTO DE DADOS")

lançamentos = [] 
num1 = []
num2 = []
num3 = []
num4 = [] 
num5 = []
num6 = []

count1 = 0
count2 = 0
count3 = 0
count4 = 0 
count5 = 0 
count6 = 0

for n in range (0, 99):
    a = randint(1, 6)
    lançamentos.append(a)

for z in lançamentos:
    if z == 1:
        count1 += 1
    if z == 2:
        count2 += 1
    if z == 3:
        count3 += 1 
    if z == 4:
        count4 += 1
    if z == 5:
        count5 += 1
    if z == 6:
        count6 +=1
        
print(lançamentos)
print("1: "+str(count1))
print("\n2: "+str(count2))
print("\n3: "+str(count3))
print("\n4: "+str(count4)) 
print("\n5: "+str(count5))
print("\n6: "+str(count6))       

    