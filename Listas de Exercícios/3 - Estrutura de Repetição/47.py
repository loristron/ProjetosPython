# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 11:37:29 2020

@author: loris

Em uma competição de ginástica, cada atleta recebe votos de sete jurados. 
A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. 
Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas 
pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima informada 
(retirar o melhor e o pior salto e depois calcular a média com as notas restantes). 

As notas não são informados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
    
Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7

Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04

"""
import statistics as stc 

vazio = False
count = 0
notas = []

while vazio == False:
    nome = input("Nome: ")
    if nome == '': 
        vazio = True
        break
    while count != 7:
        nota = float(input("Nota "+str(count+1)+": "))
        notas.append(nota)
        count += 1
    print("\nAtleta: "+nome.title())
    for n in range (0, 6):
        print("Nota "+str(n+1)+": "+str(notas[n]))
    maiorNota = max(notas)
    menorNota = min(notas)
    notas.remove(maiorNota)
    notas.remove(menorNota)
    mediaRestantes = stc.mean(notas)
    print("\nRESULTADO FINAL: ")
    print("Atela: "+nome.title())
    print("Melhor nota: "+str(maiorNota))
    print("Pior nota: "+str(menorNota))
    print("Média Final: "+str(round(mediaRestantes, 2)))    
    notas = []
    count = 0
    