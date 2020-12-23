#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
#Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) 
#deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável 
#peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável
#multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

print('Calculando a multa')
pesoPeixes = input('\nPeso do pacote em Kg: ')
if float(pesoPeixes) > 50:
	diferença =  float(pesoPeixes) - 50
	multa = diferença * 4
	print("Você ultrapassou o limite em "+str(diferença)+"kg. Sua multa será no valor de R$"+str(multa)+" reais. ")
if float(pesoPeixes) == 50:
	print("\nPor pouco! Você está exatamente no limite")
if float(pesoPeixes) < 50:
	diferença = 50 - float(pesoPeixes) 
	print("\nVocê está "+str(diferença)+"kg abaixo do limite e não precisará pagar multa. ")