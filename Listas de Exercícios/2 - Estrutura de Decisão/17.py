#Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
print("VERIFICADOR DE ANO bissexto")
ano = input("Digite o ano a ser verificado: ")
if int(ano)%4 == 0 and int(ano)%100 != 0:
	print("O ano é bissexto! ")
if int(ano)%4 != 0 or int(ano)%100 == 0:
	print("O ano em questão não é bissexto")