# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 14:38:50 2020

@author: loris

Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o 
segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. 
Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

"""

digitando = True
numeros = []
alturas = []
count = 0 
while count != 10: 
    numero = int(input("Numero do aluno: "))
    numeros.append(numero)
    altura = int(input("Altura (em cm): "))
    alturas.append(altura)
    count += 1

indexAlto = alturas.index(max(alturas))
indexBaixo = alturas.index(min(alturas))

print("Aluno mais alto:  ! COD: "+str(numeros[indexAlto])+" | Altura: "+str(max(alturas))+" cm")
print("Aluno mais baixo: ! COD: "+str(numeros[indexBaixo])+" | Altura: "+str(min(alturas))+" cm")
        