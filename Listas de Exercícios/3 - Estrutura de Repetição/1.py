#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo 
#até que o usuário informe um valor válido.

aid = True
while aid == True:
	valor = input("Insira um valor entre 0 e 10: ")
	if int(valor) < 0 or int(valor) > 10:
		print("Por favor, insira um valor válido. ")
	else:
		aid = False
print("O valor "+valor+" é válido!")

