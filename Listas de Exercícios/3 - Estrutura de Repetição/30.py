# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 17:48:22 2020

@author: loris


O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma 
loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar.
O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. 
Um valor zero deve ser informado pelo operador para indicar o final da compra. 
O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente 
forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o 
programa deverá voltar ao ponto inicial, para registrar a próxima compra. 
A saída deve ser conforme o exemplo abaixo:
    
Lojas Tabajara 
Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 9.00
Dinheiro: R$ 20.00
Troco: R$ 11.00
...


"""

def caixaRegistradora(): 
    cobrando = True
    produtos = []
    count = 0
    print("Digite 0 para a próxima ação. ")
    while cobrando == True:
        count += 1
        produto = float(input("Produto "+str(count)+" R$"))
        ivera = int(produto)
        produtos.append(round(produto, 2))
        if produto == 0:
            cobrando = False
    total = sum(produtos)
    dinheiro = float(input("Insira o valor do dinheiro recebido: R$"))
    troco = dinheiro - total
    print("Lojas Tabajara")
    n = 1
    for n in range(0, len(produtos)-1):
        print("Produto "+str(n)+" : R$"+str(produtos[n]))
    print("Total: R$"+str(sum(produtos)))
    print("Troco: R$"+str(round(troco, 2)))
    cobrando = True

caixaRegistradora()
a = int(input("Pressione 0 para retornar a operação: "))
if a == 0:
    caixaRegistradora()