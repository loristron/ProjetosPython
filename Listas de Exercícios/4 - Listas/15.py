# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 18:52:40 2020

@author: loris

Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada 
de dados quando for informado um valor igual a -1 (que não deve ser armazenado). 
Após esta entrada de dados, faça:
    
a) Mostre a quantidade de valores que foram lidos;
b) Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
c) Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
d) Calcule e mostre a soma dos valores;
e) Calcule e mostre a média dos valores;
f) Calcule e mostre a quantidade de valores acima da média calculada;
g) Calcule e mostre a quantidade de valores abaixo de sete;
h) Encerre o programa com uma mensagem;

"""
import statistics as stc 

digitando = True
numeros = [] 
vAcima = 0
vMSete = 0


print("DIGITE -1 PARA SAIR")
while digitando == True:
    ent = int(input("Insira um número: "))
    if ent == -1 :
        digitando = False
        break
    numeros.append(ent)

vlidos = len(numeros) + 1
media = stc.mean(numeros)

for n in range(0, len(numeros)):
    if numeros[n] > media:
        vAcima += 1
    if numeros[n] < 7:
        vMSete += 1


print("a) Mostre a quantidade de valores que foram lidos: "+str(vlidos)+" valores")
print("b) Exiba todos os valores na ordem em que foram informados, um ao lado do outro;")
print(numeros)
print("c) Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;")
for n in range(len(numeros), 0, -1):
    print(numeros[n-1])
print("d) Calcule e mostre a soma dos valores; "+str(sum(numeros)))
print("e) Calcule e mostre a média dos valores; "+str(round(media, 2)))
print("f) Calcule e mostre a quantidade de valores acima da média calculada; "+str(vAcima)) 
print("g) Calcule e mostre a quantidade de valores abaixo de sete; "+str(vMSete)) 
print("h) Encerre o programa com uma mensagem; ")
print("TCHAU! ")  
