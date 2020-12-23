#O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                     Até 5 Kg           Acima de 5 Kg
#File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
#Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há 
#limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um 
#desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um 
#cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e 
#valor a pagar.

print("Hipermercado Tabajara")
tipoCarne = input("Escolha entre F-Filé Duplo, A-Alcatra e P-Picanha: ")
quantidadeCarne = input("Digite a quantidade, em KG, de carne: ")
desconto = input("Vai pagar pelo cartão Tabajara? (s/n): ")

if tipoCarne == 'f' or tipoCarne == 'F':
	print("\nTipo de Carne: Filé Duplo")
	if int(quantidadeCarne) <= 5:
		precoCarne = 4.9
	if int(quantidadeCarne) > 5:
		precoCarne = 5.8
if tipoCarne == 'a' or tipoCarne == 'A':
	print("\nTipo de Carne: Alcatra")
	if int(quantidadeCarne) <= 5:
		precoCarne = 5.9
	if int(quantidadeCarne) > 5:
		precoCarne = 6.8
if tipoCarne == 'p' or tipoCarne == 'P':
	print("\nTipo de Carne: Picanha")
	if int(quantidadeCarne) <= 5:
		precoCarne = 6.9
	if int(quantidadeCarne) > 5:
		precoCarne = 7.8
precoTotal = precoCarne * int(quantidadeCarne)
print("Quantidade de carne: "+quantidadeCarne)
print("Preço da carne: R$"+str(precoCarne))
print("Valor total: R$"+str(precoTotal))
if desconto == 's' or desconto == 'S':
	valorDesconto = precoTotal * 0.05
	precoDesconto = precoTotal - valorDesconto
	print("Desconto cartão Tabajara (5%): R$"+str(round(valorDesconto, 2)))
	print("Valor final da compra: "+str(round(precoDesconto, 2)))