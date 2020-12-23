# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 15:29:42 2020

@author: loris

Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial 
várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.


"""
def fect(termo):
    print(termo)
    fat = 1
    for n in range(1, termo + 1) :
        fat *= n
    print(str(termo)+"! = "+str(fat))


rodando = True
valor = 0
while rodando == True:
    entrada = int(input("Insira um número inteiro, positivo e menor que 16 para o cálculo de fatorial:  "))
    if entrada > 0 and entrada <= 16:
        valor = fect(entrada)
    else: 
        print("Entrada inválida. Tente novamente.")
        continue
    op = input("Deseja repetir a operação? s/n ")
    if op == 's' or op == 'S':
        continue
    if op == 'n' or op == 'N':
        rodando = False
    else: 
        print("Digite uma operação válida! ")
        
            
        
    
