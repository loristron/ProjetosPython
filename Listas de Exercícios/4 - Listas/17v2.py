# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 22:46:15 2020

@author: loris

Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o 
melhor jogador após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa, que será 
utilizado pelas telefonistas, para a computação dos votos. Sua equipe foi contratada para desenvolver
este programa. Para computar cada voto, a telefonista digitará 
um número, entre 1 e 23, correspondente ao número da camisa do jogador. Um número de jogador igual zero, 
indica que a votação foi encerrada. Se um número inválido for digitado, o programa deve ignorá-lo, 
mostrando uma breve mensagem de aviso, e voltando a pedir outro número. Após o final da votação, 
o programa deverá exibir:
    
a) O total de votos computados;
b) Os númeos e respectivos votos de todos os jogadores que receberam votos;
c) O percentual de votos de cada um destes jogadores;
d) O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o 
percentual de votos dados a ele.

- Observe que os votos inválidos e o zero final não devem ser computados como votos. 
- O resultado aparece ordenado pelo número do jogador. O programa deve fazer uso de arrays. 
- O programa deverá executar o cálculo do percentual de cada jogador através de uma função. 
    - Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos.
    - A função calculará o percentual e retornará o valor calculado. 

Abaixo segue uma tela de exemplo. A disposição das informações deve ser o mais próxima possível ao exemplo. 
Os dados são fictícios e podem mudar a cada execução do programa. 

Ao final, o programa deve ainda gravar os dados referentes ao resultado da votação em um arquivo 
texto no disco, obedecendo a mesma disposição apresentada na tela.

Enquete: Quem foi o melhor jogador?

Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 11
Número do jogador (0=fim): 10
Número do jogador (0=fim): 50
Informe um valor entre 1 e 23 ou 0 para sair!
Número do jogador (0=fim): 9
Número do jogador (0=fim): 9
Número do jogador (0=fim): 0

Resultado da votação:

Foram computados 8 votos.

Jogador Votos           %
9               4               50,0%
10              3               37,5%
11              1               12,5%
O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos.

"""



digitando = True
listaEntradas = []
ordenadas = [] 
listaContagem = []
percentuais = [] 
printPercent = [] 
printNum = []
printVotos = []


def countX(lst, x): 
    count = 0
    for element in lst: 
        if element == x: 
            count += 1
    return count 

def porcentagem(numVotos, totalVotos):
    perce = numVotos / totalVotos * 100
    perce = round(perce, 2) 
    return perce

while digitando == True:
    ent = int(input("Número do jogador (0=fim): "))
    if ent == 0:
        digitando = False
        break
    if ent > 23 or ent < 0:
        print("Informe um valor entre 1 e 23 ou 0 para sair!")
        continue
    listaEntradas.append(ent)


##RESULTADO PRINTADO NA TELA:
print("\n\nResultado da votação: \n")

#a) O total de votos computados;
totalVotos = len(listaEntradas) 
print("Foram computados "+str(totalVotos)+" votos. \n")


#b) Os númeos e respectivos votos de todos os jogadores que receberam votos;
##Primeiro vou ordenar a lista dos jogadores em ordem crescente
ordenadas = sorted(listaEntradas, key=int)

for n in range (1, 24):
    votos = countX(ordenadas, n)
    if votos > 0:
        listaContagem.append(n)
        listaContagem.append(votos)

for n in range(1, len(listaContagem),2):
    pp = porcentagem(listaContagem[n], totalVotos)
    percentuais.append(listaContagem[n-1])
    percentuais.append(pp)
    

print("Jogador \tVotos \t\t %")
for n in range(0, len(listaContagem)):
    if n % 2 == 0:
        print("\n"+str(listaContagem[n]), end="")
    else:
        print("\t\t"+str(listaContagem[n]), end="")
        printVotos.append(listaContagem[n])
        print("\t\t"+str(percentuais[n]), end="")
    
#) O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de 
#votos e o percentual de votos dados a ele.    

for n in range (0, len(percentuais)):
    if n % 2 == 0:
        printNum.append(percentuais[n])
    else: 
        printPercent.append(percentuais[n])
        
        
maxVotos = listaContagem.index(max(printVotos))

print("\n\nO melhor jogador foi o número "+str(listaContagem[maxVotos-1])+", com "+str(max(printVotos))+" votos, correspondendo a "+str(max(printPercent))+"% do total de votos.")








