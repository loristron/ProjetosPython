# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 15:55:07 2020

@author: loris

Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. 
Imprima a idade e a altura na ordem inversa a ordem lida.


"""
idades = []
alturas = []

print("Idade e altura")
for n in range(0, 5):
    print("Pessoa "+str(n+1)+": ")
    idad = int(input("IDADE: "))
    idades.append(idad)
    altur = int(input("ALTURA: "))
    altuas.append(altur)

print("IDADES INVERTIDAS: "+str(idades[::-1]))
print("ALTURAS INVERTIDAS: "+str(alturas[::-1]))
