# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 22:35:53 2020

@author: loris

Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. 
Valide a entrada e permita repetir a operação.

"""
valida = False
repete = True
while repete == True: 
    popA = input("Insira a população do país A: ")
    while valida == False: 
        crescimentoA = input("Insira a taxa de crescimento, em %: ")
        if int(crescimentoA) < 0 or int(crescimentoA) > 100:
            print("Digite um valor entre 0 e 100")
        else:
            valida = True
    
    valida = False
    
    popB = input("Insira a população do país B: ")
    while valida == False: 
        crescimentoB = input("Insira a taxa de crescmento, em %, do país B: ")
        if float(crescimentoB) < 0 or float(crescimentoB) > 100:
            print("Digite um valor entre 0 e 100")
        else:
            valida = True
    
    popA = int(popA)
    cresA = int(crescimentoA) / 100
    
    popB = int(popB)
    cresB = float(crescimentoB) / 100
    
    anos = 0
    while (popA < popB):
        anos +=1
        popA = popA + (popA*cresA)
        popB = popB + (popB*cresB)
    
    print("Demorou "+str(anos)+" anos pra pop A ultrapassar B")
    repetir = input("Deseja repetir a operação? ")
    if repetir == 'n':
        repete = False

