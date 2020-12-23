#Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. 
#Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#Dicas:
#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes;

print("CLASSIFICADOR DE TRIÂNGULOS")
lados = input("Digite, separado por espaços, os lados do triângulo a ser testado:\n")
s = lados.split()
l1 = int(s[0])
l2 = int(s[1])
l3 = int(s[2])

if l1+l2 > l3 and l1+l3 > l2 and l2+l3 > l1:
	print("É um triâgulo! ")
	if l1 == l2 and l2 == l3:
		print("É um triangulo equilátero")
	if (l1 == l2 and l1 != l3) or (l1 == l3 and l1 != l2) or (l2 == l3 and l3 != l1): 
		print("É um triângulo isóceles")
	if l1 != l2 and l2 != l3 and l1 != l3:
		print("É um triângulo escaleno")
else: 
	print("Não é um triângulo! ")