# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 23:55:15 2020

@author: loris

Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados. 
O seu resultado fica sendo a média dos três valores restantes. Você deve fazer um programa que 
receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe a média
dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média). 
Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto 
não são ordenados. O programa deve ser encerrado quando não for informado o nome do atleta. 

A saída do programa deve ser conforme o exemplo abaixo:
    
Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Melhor salto:  6.5 m
Pior salto: 5.3 m
Média dos demais saltos: 5.9 m

Resultado final:
Rodrigo Curvêllo: 5.9 m


"""
import statistics as stc

saltos = []
count = 0 
nome = 'a'
vazio = False
while vazio == False:
    nome = input("Insira o nome do atleta: ")
    if nome == '':
        vazio = True
        break
    while count != 5:
        entrada = input(str(count+1)+"º Salto: ")
        slt = float(entrada)
        saltos.append(round(slt, 2))
        count += 1
        if count == 5:
            print("\nNome do atleta: "+nome.capitalize())
            for n in range(0, 5):
                print("Salto "+str(n+1)+": "+str(saltos[n])+"m")
    maiorSalto = max(saltos)
    menorSalto = min(saltos)
    saltos.remove(maiorSalto)
    saltos.remove(menorSalto)
    mediaRestante = stc.mean(saltos)
    print("O maior salto foi de "+str(maiorSalto)+"m")
    print("O pior salto foi de "+str(menorSalto)+"m")
    print("Média dos demais saltos: "+str(round(mediaRestante,2))+"m")
    print("\nResultado Final: ")
    print(nome.capitalize()+": "+str(round(mediaRestante, 2))+"m")
    count = 0
    saltos = [] 
 
    
    