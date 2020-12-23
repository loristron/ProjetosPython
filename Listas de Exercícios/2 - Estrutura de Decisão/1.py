#Faça um Programa que peça dois números e imprima o maior deles.

n1 = input("Insira o primeiro número: ")
n2 = input("Insira o segundo número: ")

if n1 > n2:
	print(str(n1)+" > "+str(n2))
if n1 < n2:
	print(str(n1)+" < "+str(n2))
if n1 == n2:
	print(str(n1)+" = "+str(n2))