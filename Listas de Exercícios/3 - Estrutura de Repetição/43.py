# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 12:30:34 2020

@author: loris

O cardápio de uma lanchonete é o seguinte:
    
Especificação   Código  Preço

Cachorro Quente 100     R$ 1,20
Hambúrguer      103     R$ 1,20

Bauru Simples   101     R$ 1,30
Cheeseburguer   104     R$ 1,30

Bauru com ovo   102     R$ 1,50

Refrigerante    105     R$ 1,00

Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. 
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. 
Considere que o cliente deve informar quando o pedido deve ser encerrado.
 
"""

listaCodigos = []
listaQuantidades = []
codigo = 1
listaProdutos = []
listaTotais = [] 
print("Digite o código 0 para calcular.")
while codigo != 0: 
    codigo = int(input("CÓDIGO: "))
    if codigo != 0 and codigo > 0:
        listaCodigos.append(codigo)    
    else:
        continue
    qtd = int(input("Quantidade: "))
    listaQuantidades.append(qtd)        


for n in range(0, len(listaCodigos)):
    if listaCodigos[n] == 100:
        preco = listaQuantidades[n] * 1.2
        listaTotais.append(round(preco, 2))
        listaProdutos.append("Cachorro Quente")
    if listaCodigos[n] == 103:
        preco = listaQuantidades[n] * 1.2
        listaTotais.append(round(preco, 2))
        listaProdutos.append("Hambúrguer")        
    if listaCodigos[n] == 101:
        preco = listaQuantidades[n] * 1.3
        listaTotais.append(round(preco, 2))
        listaProdutos.append("Bauru Simples")
    if listaCodigos[n] == 104:
        preco = listaQuantidades[n] * 1.3
        listaTotais.append(round(preco, 2))
        listaProdutos.append("Cheeseburguer")
    if listaCodigos[n] == 102:
        preco = listaQuantidades[n] * 1.5
        listaTotais.append(round(preco, 2))
        listaProdutos.append("Bauru com ovo")
    if listaCodigos[n] == 102:
        preco = listaQuantidades[n] * 1
        listaTotais.append(round(preco, 2))
        listaProdutos.append("Refrigerante")   
        

print("\nEspecificação \t\tQuantidade \t Preço\n")
for pri in range(0, len(listaQuantidades)):
    if listaProdutos[pri] == 'Cachorro Quente':
        print(listaProdutos[pri]+"\t\t"+str(listaQuantidades[pri])+" \t\t R$ "+str(listaTotais[pri]))
    else:
        print(listaProdutos[pri]+" \t\t"+str(listaQuantidades[pri])+" \t\t R$ "+str(listaTotais[pri]))
    
print("\nTotal: R$"+str(sum(listaTotais)))









