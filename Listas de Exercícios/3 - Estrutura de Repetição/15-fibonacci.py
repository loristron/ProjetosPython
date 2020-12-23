# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 14:14:52 2020

@author: loris


A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
Faça um programa capaz de gerar a série até o n−ésimo termo.


"""
entrada = int(input("Insira o n fibonacci: "))

t1 = 1
t2 = 0
t3 = 0
lista = []
for n in range(1, entrada):
    t3 = t1 + t2
    t2 = t1
    t1 = t3
    lista.append(t3)
    
print(lista)