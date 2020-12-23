# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 19:27:56 2020

@author: loris

Utilize uma lista para resolver o problema a seguir. 
Uma empresa paga seus vendedores com base em comissões. 
O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. 
Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por 
cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) 
que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
    
$200 - $299
$300 - $399
$400 - $499
$500 - $599
$600 - $699
$700 - $799
$800 - $899
$900 - $999
$1000 em diante

Desafio: Crie uma fórmula para chegar na posição da lista a partir do salário, sem fazer 
vários ifs aninhados.

"""
digitando = True
vendasBrutas = []
semanas = []
salariosTotais = []
primIntervalo = 0
segIntervalo = 0
terIntervalo = 0
qIntervalo = 0
quiIntervalo = 0
sexIntervalo = 0
setIntervalo = 0
oiIntervalo = 0
nIntervalo = 0

while digitando == True:
    v = int(input("Vendas Brutas: R$"))
    if v == 0:
        digitando = False
        break
    vendasBrutas.append(v)
    s = int(input("Semanas Trabalhadas: "))
    semanas.append(s)
    salarioTotal = (v*0.09) + s * 200 
    salariosTotais.append(round(salarioTotal,2))
    rep = input("Deseja repetir operação? s/n ")
    if rep.upper() == 'S':
        continue
    else:
        digitando = False
        break

for n in range(0, len(salariosTotais)):
    if salariosTotais[n] >= 200 and salariosTotais[n] < 300:
        primIntervalo += 1
    if salariosTotais[n] >= 300 and salariosTotais[n] < 400:
        segIntervalo += 1
    if salariosTotais[n] >= 400 and salariosTotais[n] < 500:
        terIntervalo += 1
    if salariosTotais[n] >= 500 and salariosTotais[n] < 600:
        qIntervalo += 1
    if salariosTotais[n] >= 600 and salariosTotais[n] < 700:
        quiIntervalo += 1
    if salariosTotais[n] >= 700 and salariosTotais[n] < 800:
        sexIntervalo += 1
    if salariosTotais[n] >= 800 and salariosTotais[n] < 900:
        setIntervalo += 1
    if salariosTotais[n] >= 900 and salariosTotais[n] < 1000:
        oiIntervalo += 1
    if salariosTotais[n] >= 1000:
        nIntervalo += 1

print("Intervalos: \n$200 - $299: "+str(primIntervalo)+"\n$300 - $399: "+str(segIntervalo)+"\n$400 - $499: "+str(terIntervalo)+"\n$500 - $599: "+str(qIntervalo)+"\n$600 - $699: "+str(quiIntervalo)+"\n$700 - $799: "+str(sexIntervalo)+"\n$800 - $899: "+str(setIntervalo)+"\n$900 - $999: "+str(oiIntervalo)+"\n$1000 em diante: "+str(nIntervalo))    
print(vendasBrutas)
print(salariosTotais)

    
