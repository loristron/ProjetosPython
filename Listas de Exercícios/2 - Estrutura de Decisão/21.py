#Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas 
#de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600
#reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
#Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de
# 5 e quatro notas de 1.

print("CAIXA ELETRÔNICO")
saque = input("Insira o valor a ser sacado (mínimo de R$10): R$")
if int(saque) < 10:
	print("Saque inválido! Insira um valor maior do que R$10")
if int(saque) >= 100:
	notas100 = saque[0]
	print(notas100+" notas de 100 +")
	if int(saque[1]) >= 5:
		notas50 = 1
		notas10 = int(saque[1]) - 5
		print(str(notas50)+" notas de 50 +")
		print(str(notas10)+" notas de 10 +")
	if int(saque[1]) < 5:
		notas10 = saque[1]
		print(str(notas10)+" notas de 10 +")
	if int(saque[2]) >= 5:
		notas5 = 1
		notas1 = int(saque[2]) - 5
		print(str(notas5)+" notas de 5 +")
		print(str(notas1)+" notas de 1 +")
if int(saque) < 100 and int(saque) > 9:
	notas100 = 0
	print(str(notas100)+" notas de 100 +")
	if int(saque[0]) >= 5:
		notas50 = 1 
		notas10 = int(saque[0]) - 5
		print(str(notas50)+" notas de 50 +")
		print(str(notas10)+" notas de 10 +")
	if int(saque[1]) < 5:
		notas50 = 0
		notas10 = int(saque[1])
		print(str(notas50)+" notas de 5 +")
		print(str(notas10)+" notas de 1 +")
