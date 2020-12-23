#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
#O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#par ou ímpar;
#positivo ou negativo;
#inteiro ou decimal.
print("CALCULO SIMPLES")
valor = input("Insira a operação desejada, separado por espaços: ")
s = valor.split()
if s[1] == "+":
	c = int(s[1]) + int(s[2])
	print("Resultado: "+str(c))
if s[1] == '-':
	c = int(s[0]) - int(s[2])
	print("Resultado: "+str(c))
if s[1] == '*':
	c = int(s[0]) * int(s[2])
	print("Resultado: "+str(c))
if s[1] == '/':
	c = int(s[0]) / int(s[2])
	print("Resultado: "+str(c))

