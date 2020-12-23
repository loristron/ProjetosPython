# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 14:10:18 2020

@author: loris

Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
imprima o número de alunos com média maior ou igual a 7.0.


"""
import statistics as stc

notas = []
medias = []
maiorQSete = 0

print("4 notas de 10 alunos")

for n in range(0, 10):
    print("Aluno "+str(n+1)+": ")
    for i in range(0, 4):
        ent = int(input("Insira a nota "+str(i+1)+": "))
        notas.append(ent)
        if i == 3:
            media = stc.mean(notas)
            medias.append(round(media, 2))
            
for h in range(0,10):
    if h >= 7:
        maiorQSete += 1
        
print("\nA turma teve "+str(maiorQSete)+" médias maiores do que 7.")
