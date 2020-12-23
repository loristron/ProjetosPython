# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 22:00:20 2020

@author: loris

#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd'; 

"""

validaNome = False
validaIdade = False
validaSalario = False
validaSexo = False
validaEstado = False

while validaNome == False:
    nome = input("Nome: ")
    if len(nome) > 3:
        validaNome = True
    else:
        print("Nome precisa ter mais de 3 caracteres.")
while validaIdade == False:
    idade = input("Idade: ")
    if int(idade) >= 0 and int(idade) <= 150:
        validaIdade = True
    else:
        print("Idade precisa ser entre 0 e 150 anos")
while validaSalario == False:
    salario = input("Salário: ")
    if int(salario) > 0:
        validaSalario = True
    else:
        print("Salário precisa ser maior que zero")
while validaSexo == False:
    sexo = input("Sexo: ")
    if sexo == 'm' or sexo == 'f':
        validaSexo = True
    else:
        print("Sexo precisa ser 'm ou 'f'")
while validaEstado == False:
    estado = input("Estado civil: ")
    if estado == 's' or estado =='c' or estado == 'v' or estado == 'd':
        validaEstado = True
    else:
        print("Estado civil precisa ser 's', 'c', 'v' ou 'd ")
        
print("Todas as informações foram validadas! ")
        
            