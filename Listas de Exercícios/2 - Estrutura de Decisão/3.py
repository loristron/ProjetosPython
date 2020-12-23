#Faça um Programa que verifique se uma letra digitada 
#é "F" ou "M". Conforme a letra escrever:
#F - Feminino, M - Masculino, Sexo Inválido.

letra = input("Digite F ou M: ")
if letra == 'F' or letra == 'f':
	print("SEXO FEMININO")
if letra == 'M' or letra == 'm':
	print("SEXO MASCULINO")
if letra != 'm' and letra != 'M' and letra != 'f' and letra != 'F':
	print("Letra inválida")

