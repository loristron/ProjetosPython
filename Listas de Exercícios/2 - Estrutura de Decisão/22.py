#Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).

print("PAR OU ÍMPAR")
entrada = input("Insira um número inteiro: ")
num = int(entrada)
if num%2 == 0:
	print("O número é par!")
else:
	print("O número é ímpar")
