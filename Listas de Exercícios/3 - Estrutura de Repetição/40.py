# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 14:45:32 2020

@author: loris

Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito.
Foram obtidos os seguintes dados:
    
Código da cidade;
Número de veículos de passeio (em 1999);
Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
Qual a média de veículos nas cinco cidades juntas;
Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

"""

import statistics as stc

count = 0
codigos = []
veiculos = []
acidentes = []
indices = [] 
menosDoisMil = []

while count != 3:
    codigo = input("Código: ")
    codigos.append(codigo)
    numVeiculos = int(input("Veículos de passeio: "))
    veiculos.append(numVeiculos)
    numAcidentes = int(input("Número de acidentes: ")) 
    acidentes.append(numAcidentes)
    count += 1

for n in range(0, len(codigos)): 
    indice = acidentes[n] / veiculos[n]
    indices.append(round(indice, 2))

print(indices)

mediaVeiculos = stc.mean(veiculos) 
maisAcidentes = indices.index(max(indices))
menosAcidentes = indices.index(min(indices))

#Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
print("O maior índicie de  pertence a "+str(codigos[maisAcidentes])+", com indicie de "+str(max(indices)*100)+" %")
print("O menor indice de  pertence a "+str(codigos[menosAcidentes])+", com indicie de "+str(min(indices)*100)+" %")
#Qual a média de veículos nas cinco cidades juntas;
print("A média de veículos é de: "+str(round(mediaVeiculos, 2))+" carros por cidade")

#Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

for n in range(0, len(veiculos) - 1):
    if veiculos[n] <= 2000:
        menosDoisMil.append(acidentes[n])

mediaMenosDoismil = stc.mean(menosDoisMil)
print("A media de acidentes com menos de 2000 veiculos é: "+str(round(mediaMenosDoismil, 2))+" acidentes por ano")
        
    
    