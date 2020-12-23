# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 12:28:22 2020

@author: loris

Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
Faça um programa que determine o salário atual desse funcionário. 
Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.

"""


anoInicial = 1996
aumento = 0.15
salarioFinal = 0
count = 0
#A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.

salarioInicial = int(input("Digite o salário inicial: "))

for n in range(1996, 2021):
    count += 1
    if n == 1996: 
        salarioFinal = salarioInicial + (salarioInicial * aumento)
    if n >= 1997:
        print("ano = "+str(n))
        print(count)
        reajuste = round((aumento * count), 2)
        print("Reajuste: "+str(reajuste)+" %")
        salarioFinal = salarioFinal + (salarioFinal * reajuste)
        print(salarioFinal)