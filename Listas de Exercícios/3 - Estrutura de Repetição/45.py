# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 15:22:30 2020

@author: loris

Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, 
o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o 
gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa).
Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema.
Após todos os alunos terem respondido informar:
    
-Maior e Menor Acerto;
-Total de Alunos que utilizaram o sistema;
-A Média das Notas da Turma.

Gabarito da Prova:
01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A

Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da 
prova antes dos alunos usarem o programa.
"""


import statistics as stc

count = 0
respostas = []
notas = [] 
acertos = 0
gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']
continua = 'S'

while continua.upper() == 'S':
    print("INSIRA A RESPOSTA DE CADA QUESTÃO: ")
    while count != 10:
        res = input(str(count+1)+" - ")
        respostas.insert(0+count, res.upper())
        print(respostas)
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
