# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 13:31:42 2020

@author: loris

Em uma eleição presidencial existem quatro candidatos. 

Os votos são informados por meio de código. Os códigos utilizados são:
1 , 2, 3, 4  - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco

Faça um programa que calcule e mostre:
-O total de votos para cada candidato;
-O total de votos nulos;
-O total de votos em branco;
-A percentagem de votos nulos sobre o total de votos;
-A percentagem de votos em branco sobre o total de votos.

Para finalizar o conjunto de votos tem-se o valor zero.

"""

print("VOTE 0 PARA ENCERRAR")

votacao = True
votos = []
vJoao = 0
vJose = 0
vGeraldo = 0
vMiguel = 0
vBranco = 0
vNulo = 0

while votacao == True:
    voto = int(input("VOTE: \n1) Joao\n2)Jose\n3)Geraldo\n4)Miguel\n\n5)NULO\n6)VOTO EM BRANCO\n"))
    if voto != 0 and voto <= 6:
        votos.append(voto)
    if voto == 0:
        votacao = False
        continue
    
print(votos)
for n in votos:
    if n == 1:
        vJoao += 1
    if n == 2:
        vJose += 1
    if n == 3:
        vGeraldo += 1
    if n == 4:
        vMiguel += 1
    if n == 5:
        vNulo += 1
    if n == 6:
        vBranco += 1

totalVotos = len(votos)
pNulo = vNulo / totalVotos * 100
pBranco = vBranco / totalVotos * 100

print("\nRESULTADO")        
print("1) João - "+str(vJoao)+" votos")
print("2) José - "+str(vJose)+" votos")
print("3) Geraldo - "+str(vGeraldo)+" votos")
print("4) Miguel - "+str(vMiguel)+" votos")
print("5) NULO - "+str(vNulo)+" votos")
print("6) BRANCOS - "+str(vBranco)+" votos")
print("\nTOTAL DE VOTOS VÁLIDOS: "+str(totalVotos))
print("PERCENTUAL VOTOS NULOS: "+str(round(pNulo,2))+"% ")
print("PERCENTUAL VOTOS BRANCOS: "+str(round(pBranco,2))+"% ")

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    