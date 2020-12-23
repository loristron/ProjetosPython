#Faça um Programa que leia um número e exiba o dia correspondente da semana. 
#(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

print("DIA DA SEMANA")
entrada = input("Insira um número de 1 à 7: ")
s = int(entrada)

if s == 1:
	print("Domingo!")
elif s == 2:
	print("Segunda!")
elif s == 3: 
	print("Terça!")
elif s == 4: 
	print("Quarta!")
elif s == 5:
	print("Quinta!")
elif s == 6:
	print("Sexta!")
else: 
	print("Insira um valor válido!")