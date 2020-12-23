#Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#Álcool:
#até 20 litros, desconto de 3% por litro
#acima de 20 litros, desconto de 5% por litro
#Gasolina:
#até 20 litros, desconto de 4% por litro
#acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível 
#(codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do 
#litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

print("POSTO DE GASOLINA")
litros = input("Quantos litros você quer comprar? ")
combustivel = input("Qual o combustivel? Utilize A-Álcool ou G-Gasolina. ")
if combustivel == 'a' or combustivel == 'A':
	if int(litros) <= 20:
		precoL = 1.9 - (1.9 * 0.03)
		precoFinal = int(litros) * precoL
		print("O praço a ser pago pelo combustivel é de R$"+str(round(precoFinal,2)))
	if int(litros) > 20:
		precoL = 1.9 - (1.9 * 0.05)
		precoFinal = int(litros) * precoL
		print("O praço a ser pago pelo combustivel é de R$"+str(round(precoFinal,2)))
if combustivel == 'g' or combustivel == 'G':
	if int(litros) <= 20:
		precoL = 2.5 - (2.5 * 0.04)
		precoFinal = int(litros) * precoL
		print("O praço a ser pago pelo combustivel é de R$"+str(round(precoFinal,2)))
	if int(litros) > 20:
		precoL = 2.5 - (2.5 * 0.06)
		precoFinal = int(litros) * precoL
		print("O praço a ser pago pelo combustivel é de R$"+str(round(precoFinal,2)))
