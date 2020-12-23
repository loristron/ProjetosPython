#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
#Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

print("TURNOS DE ESTUDO")
entrada = input("Em que turno você estuda? Digite 'M' para matutino, 'V' para Vespertino e 'N' para Noturno: ")
valor = entrada.lower()
if valor == 'm':
	print("Bom dia!")
elif valor == 'v':
	print("Boa tarde!")
elif valor == 'n':
	print("Boa noite!")
else:
	print("Valor Inválido!")