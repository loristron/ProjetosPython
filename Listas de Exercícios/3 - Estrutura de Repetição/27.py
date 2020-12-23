# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 17:32:40 2020

@author: loris

Faça um programa que calcule o número médio de alunos por turma. 
Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. 
As turmas não podem ter mais de 40 alunos.


"""
import statistics as srt

print("MÉDIA DE ALUNOS POR TURMA")

qtdTurmas = int(input("Insira a quantidade de turmas: "))

count = 0
lista = []

while count != qtdTurmas:
    alunos = int(input("Insira a quantidade de alunos: "))
    if alunos <= 40:
        lista.append(alunos)
        count += 1
    else:
        print("Não computado. ")

media = srt.mean(lista)
print("\nA média de alunos por turma é de "+str(round(media, 2))+" pessoas.")
    