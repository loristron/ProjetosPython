#Faça um Programa que peça um valor e mostre na tela se 
#o valor é positivo ou negativo.

print('POSITIVO OU NEGATIVO')
valor = input('Insira um número: ')

if float(valor) < 0:
	print("O número que você inseriu é negativo")
if float(valor) > 0:
	print("O valor que você inseriu é positivo")
if float(valor) == 0:
	print("O valor que você inseriu é igual a 0")