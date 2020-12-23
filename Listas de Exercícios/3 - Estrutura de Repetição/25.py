# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 17:00:05 2020

@author: loris

Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a
média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60;
e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.


"""
import statistics as stc

repete = True
lista = []
print("Digite n para encerrar")
while repete == True:
    entrada = input("Insira uma idade: ")
    if entrada == 'n' or entrada == 'N':
        repete = False
        continue
    numero = int(entrada)
    lista.append(numero)

media = stc.mean(lista)
print("A média da turma é de "+str(round(media,2))+" anos")
if media >= 0 and media <= 25:
    print("A turma é jovem! ")
if media >= 26 and media <= 60:
    print("A turma é adulta! ")
if media > 60:
    print("A turma é idosa!")