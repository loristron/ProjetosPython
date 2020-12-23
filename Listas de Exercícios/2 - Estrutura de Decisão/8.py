#Faça um programa que pergunte o preço de três produtos e 
#informe qual produto você deve comprar, sabendo que a decisão 
#é sempre pelo mais barato.

print("ORÇAMENTOS")
p1 = input("\nInsira o primeiro preço: ")
p2 = input("Insira o segundo preço: ")
p3 = input("Insira o terceiro preço: ")

if p1 < p2 and p1 < p3: 
	print("Compre o primeiro produto no valor de "+str(p1))
if p2 < p1 and p2 < p3:
	print("Compre o segundo produto no valor de "+str(p2))
if p3 < p1 and p3 < p2: 
	print("Compre o terceiro produto no valor de "+str(p3))