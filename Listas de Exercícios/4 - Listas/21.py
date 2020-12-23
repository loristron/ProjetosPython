# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 15:21:30 2020

@author: loris

Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: 
FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o consumo desses carros, isto é, quantos 
quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:
    
O modelo do carro mais econômico;
Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 
1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. 
Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao 
exemplo. Os dados são fictícios e podem mudar a cada execução do programa.

Comparativo de Consumo de Combustível

Veículo 1
Nome: fusca
Km por litro: 7

Veículo 2
Nome: gol
Km por litro: 10

Veículo 3
Nome: uno
Km por litro: 12.5

Veículo 4
Nome: Vectra
Km por litro: 9

Veículo 5
Nome: Peugeout
Km por litro: 14.5

Relatório Final
 1 - fusca           -    7.0 -  142.9 litros - R$ 321.43
 2 - gol             -   10.0 -  100.0 litros - R$ 225.00
 3 - uno             -   12.5 -   80.0 litros - R$ 180.00
 4 - vectra          -    9.0 -  111.1 litros - R$ 250.00
 5 - peugeout        -   14.5 -   69.0 litros - R$ 155.17

O menor consumo é do peugeout.

"""

gasolina = 2.25
count = 1
digitando = True
nomesCarros = []
kilometragem = []
consumos = []
precos = []

#COLETA DE DADOS
print("Comparativo de Consumo de Combustível")
while digitando == True:
    print("Veículo "+str(count))
    nome = input("Nome: ")
    if nome == '':
        digitando = False
        break
    nomesCarros.append(nome)
    km = float(input("Km por litro: "))
    kilometragem.append(km)
    count += 1

#Quanto custa pra percorrer, em cada carro, 1000 KM
for n in range(0, len(nomesCarros)):
    consu = 1000 / kilometragem[n]
    consu = round(consu, 2)
    consumos.append(consu)
    prec = consu * gasolina
    prec = round(prec, 2)
    precos.append(prec)    
    
#Mostrando os resultados    
print("\nRelatório Final: ")
print("ID\tNome\tKm/L\tConsumo 1000KM\t\tPreco")
for n in range(0, len(nomesCarros)):
    print(str(n)+" - ", end='\t')
    print(str(nomesCarros[n])+" - ", end="")
    print(str(kilometragem[n]), end="\t")
    print(str(consumos[n])+" litros", end="\t\t")
    print("R$ "+str(precos[n]))
    

    
    
    
    
    
    
    
    
    

