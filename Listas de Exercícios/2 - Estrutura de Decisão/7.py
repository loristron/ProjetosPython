#Faça um Programa que leia três números e mostre o 
#maior e o menor deles.
while True:
	valor = input("Insira três numeros: ")
	s = valor.split()

	n1 = s[0]
	n2 = s[1]
	n3 = s[2]

	if n1 > n2 and n1 > n3:
		print("O maior número digitado é "+str(n1))
	if n2 > n1 and n2 > n3:
		print("O maior número digitado é "+str(n2))
	if n3 > n2 and n3 > n1:
		print("O maior número digitado é "+str(n3))
	if n1 < n2 and n1 < n3:
		print("O menor número digitadp é "+str(n1))
	if n2 < n1 and n2 < n3:
		print("O menor número digitado é "+str(n2))
	if n3 < n1 and n3 < n2:
		print("O menor número digitado é "+str(n3))