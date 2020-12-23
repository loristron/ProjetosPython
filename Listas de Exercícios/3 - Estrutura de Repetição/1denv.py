# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 21:26:59 2020

@author: loris
"""


#Faça um programa que peça uma nota, entre zero e dez. 
#Mostre uma mensagem caso o valor seja inválido e continue 
#pedindo até que o usuário informe um valor válido.

certo = False

while certo == False:
    entrada = input("Insira uma nota entre 0 e 10: ")
    if (int(entrada) >=0 and int(entrada) <= 10):
        print("Você digitou um valor válido!")
        certo = True
    else:
        print("Nope! Digite um valor válido.")



