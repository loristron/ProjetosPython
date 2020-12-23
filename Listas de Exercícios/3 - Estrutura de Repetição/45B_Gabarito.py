# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 23:48:29 2020

@author: loris
"""


import statistics as stc

count = 0
respostas = []
gabarito = []
notas = [] 
acertos = 0
continua = 'S'

print("ÁREA DO PROFESSOR")
for n in range (1, 11):
    gab = input("Questão "+str(n)+") ")
    gabarito.append(gab.upper())

while continua.upper() == 'S':
    print("INSIRA A RESPOSTA DE CADA QUESTÃO: ")
    while count != 10:
        res = input(str(count+1)+" - ")
        respostas.insert(0+count, res.upper())
        count += 1
    for n in range(0, len(respostas)):
            if respostas[n] == gabarito[n]:
                acertos += 1 

    notas.append(acertos)
    acertos = 0
    contador += 1
    print("A nota total foi de : "+str(notas[-1]))
    continua = input("Deseja adicionar outra nota? s/n ")
    if continua.upper() == 'S':
        respostas[0:10] = []
        count = 0
        continue
    else:
        continua = 'N'
        break
mediaNotas = stc.mean(notas)
print(notas)
print("O maior numero de acertos foi: "+str(max(notas))+"")
print("O menor numero de acertos foi "+str(min(notas))+"")
print("A média da turma é de "+str(round(mediaNotas, 2)))
