# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:54:53 2020

@author: loris


Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo 
e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código,
sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo 
código. Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo,
do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes

"""

import statistics as srt
digitando = True
codigos = []
pesos = []
alturas = []

print("Digite código 0 para calcular.")
while digitando == True:
    codigo = int(input("Código: "))
    if codigo == 0:
        digitando = False
        continue
    codigos.append(codigo)
    altura = int(input("Altura (em cm): "))
    alturas.append(altura)
    peso = int(input("Peso (em Kg): ")) 
    pesos.append(peso)  
 
indexAlto = alturas.index(max(alturas))
indexBaixo = alturas.index(min(alturas))
indexLeve = pesos.index(min(pesos))
indexPesado = pesos.index(max(pesos))

mediaAlturas = srt.mean(alturas)
mediaPesos = srt.mean(pesos)

print("Mais alto:   | COD: "+str(codigos[indexAlto])+" | Altura: "+str(max(alturas))+" cm ")
print("Mais baixo:  | COD: "+str(codigos[indexBaixo])+" | Altura: "+str(min(alturas))+" cm")
print("Mais leve:   | COD: "+str(codigos[indexLeve])+" | Altura: "+str(min(pesos))+" kg")
print("Mais pesado: | COD: "+str(codigos[indexPesado])+" | Altura: "+str(max(pesos))+" kg")
print("MÉDIA DE PESO: "+str(mediaPesos)+" kg")
print("MÉDIA ALTURAS: "+str(mediaAlturas)+" cm")
