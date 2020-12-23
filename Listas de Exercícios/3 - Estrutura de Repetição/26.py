# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 17:06:42 2020

@author: loris

Numa eleição existem três candidatos. 
Faça um programa que peça o número total de eleitores. 
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.


"""


qtdEleitores = int(input("Insira a quantidade de eleitores: "))

count = 1
candA = 0
candB = 0
candC = 0

while count != qtdEleitores + 1:
    print("\nVOTO DO ELEITOR "+str(count))
    voto = input("VOTE: \n(A) Candidato A\n(B) Candidato B\n(C) Candidato C\n")
    if voto == 'A' or voto == 'a':
        candA += 1
        print("Voto computado com Sucesso!")
        count += 1
        
    if voto == 'B' or voto == 'b':
        candB += 1
        print("Voto computado com Sucesso!")
        count += 1
        
    if voto == 'C' or voto == 'c':
        candC += 1
        print("Voto computado com sucesso! ")
        count += 1
    else:
        print("Esse candidato não disputa essa eleição.")

print("O Candidato A teve "+str(candA)+" votos.")
print("O Candidato B teve "+str(candB)+" votos.")
print("O Candidato C teve "+str(candC)+" votos.")
