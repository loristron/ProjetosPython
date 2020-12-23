#Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
#Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
#326 = 3 centenas, 2 dezenas e 6 unidades
#12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

print("PROGRAMA DIVISOR EM CENTENAS, DEZENAS E UNIDADES")
num = input("Insira um número inteiro menor do que 1000: ")

if int(num) <= 1000:
	if int(num) >= 100:
		centenas = int(num[0])
		dezenas = int(num[1])
		unidades = int(num[2])
		if centenas > 1 and dezenas > 1 and unidades > 1:
			print(num+" = "+str(centenas)+" centenas, "+str(dezenas)+" dezenas e "+str(unidades)+" unidades")
		if centenas > 1 and dezenas == 1 and unidades > 1:
			print(num+" = "+str(centenas)+" centenas, "+str(dezenas)+" dezena e "+str(unidades)+" unidades")
		if centenas > 1 and dezenas > 1 and unidades == 1:
			print(num+" = "+str(centenas)+" centenas, "+str(dezenas)+" dezenas e "+str(unidades)+" unidade.")
		if centenas > 1 and dezenas == 1 and unidades == 1:
			print(num+" = "+str(centenas)+" centenas, "+str(dezenas)+" dezena e "+str(unidades)+" unidade.")
		if centenas > 1 and dezenas == 0 and unidades > 1:
			print(num+" = "+str(centenas)+" centenas e "+str(unidades)+" unidades.")
		if centenas > 1 and dezenas > 1 and unidades == 0:
			print(num+" = "+str(centenas)+" centenas e "+str(dezenas)+" dezenas. ")
		if centenas > 1 and dezenas ==0 and unidades == 0:
			print(num+" = "+str(centenas)+" centenas.")
		if centenas == 1 and dezenas > 1 and unidades > 1:
			print(num+" = "+str(centenas)+" centena, "+str(dezenas)+" dezenas e "+str(unidades)+" unidades")
		if centenas == 1 and dezenas > 1 and unidades == 1:
			print(num+" = "+str(centenas)+" centena, "+str(dezenas)+" dezenas e "+str(unidades)+" unidade.")
		if centenas == 1 and dezenas == 1 and unidades > 1:
			print(num+" = "+str(centenas)+" centena, "+str(dezenas)+" dezena e "+str(unidades)+" unidades")
		if centenas == 1 and dezenas == 1 and unidades == 1: 
			print(num+" = "+str(centenas)+" centena, "+str(dezenas)+" dezena e "+str(unidades)+" unidade")
		if centenas == 1 and dezenas == 0 and unidades == 0:
			print(num+" = "+str(centenas)+" centena.")
		if centenas > 1 and dezenas == 1 and unidades == 0:
			print(num+" = "+str(centenas)+" centenas e "+str(dezenas)+" dezena.")
		if (centenas > 1 and dezenas == 0 and unidades == 1): 
			print(num+" = "+str(centenas)+" centenas e "+str(unidades)+" unidade.")
		if centenas == 1 and dezenas == 0 and unidades == 1:
			print(num+" = "+str(centenas)+" centenas e "+str(unidades)+" unidade.")



	if int(num) < 100  and int(num) > 9:
		dezenas = int(num[0])
		unidades = int(num[1])
		if dezenas > 1 and unidades > 1:
			print(num+" = "+str(dezenas)+" dezenas e "+str(unidades)+" unidades.")
		if dezenas > 1 and unidades == 1:
			print(num+" = "+str(dezenas)+" dezenas e "+str(unidades)+" unidade.")
		if dezenas == 1 and unidades > 1:
			print(num+" = "+str(dezenas)+" dezena e "+str(unidades)+" unidades")
		if dezenas == 1 and unidades == 1:
			print(num+" = "+str(dezenas)+" dezena e "+str(unidades)+" unidades")
		if dezenas > 1 and unidades == 0:
			print(num+" = "+str(dezenas)+" dezenas.")
		if dezenas == 1 and unidades == 0:
			print(num+" = "+str(dezenas)+" dezena.")

	if int(num) < 10:
		unidades = int(num[0])
		if unidades > 1:
			print(num+" = "+str(unidades)+" unidades.")
		if unidades == 1: 
			print (num+" = "+str(unidades)+" unidade. ")


