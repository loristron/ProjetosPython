# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 16:49:48 2020

@author: loris

Foram anotadas as idades e alturas de 30 alunos. 
Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura 
inferior à média de altura desses alunos.


"""
import random 
import statistics as stc

alturasRand = random.sample(range(100, 160), 30) 
idadesRand = random.sample(range(1, 100), 30)
count = 0 

mediaAlturas = stc.mean(alturasRand)

for n in range(0, 30):
    if idadesRand[n] > 13 and alturasRand[n] < mediaAlturas:
        count += 1 

print(alturasRand)
print(idadesRand)
print(str(count)+" alunos possuem altura menor que a média de "+str(round(mediaAlturas, 2))+" cm e têm mais que 13 anos")

