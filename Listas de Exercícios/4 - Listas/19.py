# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 12:16:08 2020

@author: loris

Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade
de organizações:

"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro

Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final 
o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a 
entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). 
Os valores referentes a cada uma das opções devem ser armazenados num vetor. 
Após os dados terem sido completamente informados, o programa deverá calcular a percentual de 
cada um dos concorrentes e informar o vencedor da enquete. 
O formato da saída foi dado pela empresa, e é o seguinte:
    

Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----
Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.

"""
digitando = True
listaSistemas = ["Windows Server", "Unix", "Linux", "Netware", "Mac OS", "Outro"]
listaEntradas = []
listaContagemVotos = [] 
listaPercentagem = []



def countX(x, lista):
    count = 0
    for n in lista:
        if x == n :
            count += 1
    return count

def porcentagem(x, total):
    perce = 0
    perce = x / total * 100
    perce = round(perce, 2)
    return perce



while digitando == True:
    ent = int(input("Insira seu sistema operacional (1 a 6, 0 = fim):  "))
    if ent != 0 and ent <= 6:
        listaEntradas.append(ent)
    if ent == 0:
        digitando = False
        break

totalVotos = len(listaEntradas)
    
for n in range (1, 7):
    contVotos = countX(n, listaEntradas)
    listaContagemVotos.append(contVotos)
    porce = porcentagem(contVotos, totalVotos)
    listaPercentagem.append(porce) 
    
    
print("---------------------------------------------------")
print("Sistema Operacional\tVotos\t\t%")
for n in range (0, 6):
        print("---------------------------------------------------")
        print(str(listaSistemas[n]), end="")
        if n == 0:
            print("\t\t"+str(listaContagemVotos[n]), end="")
            print("\t\t"+str(listaPercentagem[n]))
        else:
            print("\t\t\t"+str(listaContagemVotos[n]), end="")
            print("\t\t"+str(listaPercentagem[n]))
print("---------------------------------------------------")
print("Total\t\t\t\t\t"+str(totalVotos))       

indexMax = listaPercentagem.index(max(listaPercentagem))

print("O Sistema Operacional mais votado foi o "+str(listaSistemas[indexMax])+" com "+str(max(listaContagemVotos))+" votos, correspondendo a "+str(max(listaPercentagem))+"% dos votos.")            
        
    
    
