# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 18:25:20 2020

@author: loris

Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
    
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" 

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".


"""
res = []
sus = 0

print("SUSPEITOS DE UM CRIME")
ent = input("Telefonou para a vítima? ")
res.append(ent.upper())
ent = input("Esteve no local do crime? ")
res.append(ent.upper())
ent = input("Mora perto da vítima? ")
res.append(ent.upper())
ent = input("Devia para a vítima? ")
res.append(ent.upper())
ent = input("Já trabalhou com a vítima? ")
res.append(ent.upper())

for n in range(0, len(res)):
    if res[n] == 'S':
        sus += 1
if sus == 2:
    print("SUSPEITO!")
if sus >= 3 and sus <= 4:
    print("CÚMPLICE!")
if sus == 5:
    print("ASSASSINO!!")
if sus == 0:
    print("Inocente! ")      