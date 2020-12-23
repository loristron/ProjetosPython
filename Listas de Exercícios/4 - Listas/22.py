# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 15:56:26 2020

@author: loris

Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção 
de fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os 
cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o 
que se pode aproveitar deles.
Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá 
receber um número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o 
tipo de defeito:
    
necessita da esfera;
necessita de limpeza; 
a.necessita troca do cabo ou conector; 
a.quebrado ou inutilizado Uma identificação igual a zero encerra o programa. 
Ao final o programa deverá emitir o seguinte relatório:
    

Quantidade de mouses: 100

Situação                        Quantidade              Percentual
1- necessita da esfera                  40                     40%
2- necessita de limpeza                 30                     30%
3- necessita troca do cabo ou conector  15                     15%
4- quebrado ou inutilizado              15                     15%

"""

digitando = True
lstReparos = ["1 - Necessita da Esfera", "2 -Necessita de Limpeza", "3 -Necessita Troca do Cabo", "4 -Inutilizado ou Quebrado"]
lstEntradas = [] 
lstQuantidades = [] 
lstPercentuais = []

def countX(x, lst):
    count = 0
    for x in lst:
        if x == n:
            count += 1
    return count

print("1- necessita da esfera  ")
print("2- necessita de limpeza")
print("3- necessita troca do cabo ou conector")
print("4- quebrado ou inutilizado")
print("Digite 0 para finalizar")

#Coletando Entradas
while digitando == True:
    ent = int(input("Situação: "))
    if ent != 0 and ent < 5:
        lstEntradas.append(ent)
    if ent == 0:
        digitando = False
        break
print(lstEntradas)
quantidade = len(lstEntradas)


#Lista Quantidades
for n in range(1, 5):
    cont = countX(n, lstEntradas)
    lstQuantidades.append(cont)
print(lstQuantidades)

#Lista Percentuais
for n in range(0, 4):
     p = lstQuantidades[n] / quantidade * 100 
     p = round(p, 2)
     lstPercentuais.append(p)
     
print(lstPercentuais)

#printando os resultados
print("Quantidade de mouses: "+str(quantidade))
print("Situação\t\t\tQuantidade\tPercentual")

for n in range(0, 4):
    print(str(lstReparos[n]), end="\t\t\t")
    print(str(lstQuantidades[n]), end="\t\t")
    print(str(lstPercentuais[n]))
   
    
    




    