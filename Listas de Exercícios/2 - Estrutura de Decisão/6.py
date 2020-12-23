#Faça um Programa que leia três números e mostre o maior deles.
while True:
	print("POR LINHA: ")
	linha = input("Digite três números: ")
	s = linha.split()
	n1 = int(s[0])
	n2 = int(s[1])
	n3 = int(s[2])
	if n1 > n2 and n1 > n3:
		print("O maior número digitado é "+str(n1))
	if n2 > n1 and n2 > n3:
		print("O maior número digitado é "+str(n2))
	if n3 > n1 and n3 > n2: 
		print("O maior número digitado é "+str(n3))
