#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

print("DATA VÁLIDA")
data = input("Insira uma data no formato dd/mm/aaaa: ")
if data[2] != '/' or data[5] != '/':
	print("erro nas suas barras! ")
s = data.split("/")
if int(s[0]) > 0 and int(s[0]) <= 31:
	if int(s[1]) > 0 and int(s[1]) <= 12:
		print("Sua data é válida!")
	else: 
		print("Sua data é inválida!")
else:
	print("Sua data é inválida")