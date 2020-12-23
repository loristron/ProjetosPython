#Faça um Programa que leia três números e mostre-os em ordem 
#crescente.
print("ORDEM DECRESCENTE")
e1 = input("Insira o primeiro número: ")
e2 = input("Insira o segundo número: ")
e3 = input("Insira o terceiro número: ")

n1 = int(e1)
n2 = int(e2)
n3 = int(e3)

#N1 MAIOR
#n1 > n2 > n3 
#n1 > n3 > n2
#n1 > n2 = n3
if n1 > n2 and n2 > n3:
	print("ORDEM CRESCENTE: "+str(n3)+", "+str(n2)+" e "+str(n1))
if n1 > n3 and n3 > n2:
	print("ORDEM CRESCENTE: "+str(n2)+" , "+str(n3)+" e "+str(n1))
if n1 > n2 and n2 == n3:
	print("ORDEMDECRESCENTE: "+str(n2)+" , "+str(n1))

#N2 MAIOR
#n2 > n1 > n3
#n2 > n3 > n1
#n2 > n3 = n1
if n2 > n1 and n1 > n3:
	print("ORDEM CRESCENTE: "+str(n3)+", "+str(n1)+" e "+str(n2))
if n2 > n3 and n3 > n1: 
	print("ORDEM CRESCENTE: "+str(n1)+", "+str(n3)+" e "+str(n1))
if n2 > n3 and n3 == n1:
	print("ORDEM CRESCENTE: "+str(n1)+" e "+str(n2))

#N3 MAIOR
#n3 > n1 > n2
#n3 > n2 > n1
#n3 > n1 = n2
if n3 > n1 and n1 > n2:
	print("ORDEM CRESCENTE: "+str(n2)+", "+str(n1)+" e "+str(n3))
if n3 > n2 and n2 > n1:
	print("ORDEM CRESCENTE: "+str(n1)+", "+str(n2)+" e "+str(n3))
if n3 > n1 and n1 == n2:
	print("ORDEM CRESCENTE: "+str(n1)+" e "+str(n3))




