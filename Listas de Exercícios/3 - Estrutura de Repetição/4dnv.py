# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 22:18:53 2020

@author: loris

Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de 
crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. 
Faça um programa que calcule e escreva o número de anos necessários para que a população do país A 
ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

"""


popA = 80000
crescimentoA = 0.03

popB = 200000
crescimentoB = 0.015

anos = 0
while (popA < popB):
    anos = anos + 1
    popA = popA + (popA*crescimentoA)
    popB = popB + (popB*crescimentoB)
an = str(anos)

print("Demorou "+an+" anos pra pop A ultrapassar B")
  