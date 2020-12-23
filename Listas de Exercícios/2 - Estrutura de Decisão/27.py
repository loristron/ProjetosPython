#Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                      Até 5 Kg           Acima de 5 Kg
#Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% 
#sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o 
#valor a ser pago pelo cliente.
print("FRUTEIRA")
kgMorango = input("Insira a quantidade de morangos: ")
kgMaca = input("Insira a quantidade de maças: ")

if int(kgMaca) <= 5:
	precoMaca = 1.8
if int(kgMaca) > 5:
	precoMaca = 1.5
if int(kgMorango) <= 5:
	precoMorango = 2.5
if int(kgMorango) > 5:
	precoMorango = 2.2

quilosTotais = int(kgMaca) + int(kgMorango)
valorTotal = (int(kgMaca) * precoMaca) + (int(kgMorango) * precoMorango)
if valorTotal > 25 or quilosTotais > 8:
	valorTotalDescontado = valorTotal - (valorTotal * 0.1)
	print("O valor total do seu pedido será de R$"+str(valorTotalDescontado))
else: 
	print("O valor total de sua compra é de R$"+str(valorTotal))
