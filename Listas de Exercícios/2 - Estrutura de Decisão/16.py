#Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
#O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
#Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer 
#pedir os demais valores, sendo encerrado;
#Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;


print("EQUAÇÃO DE SEGUNDO GRAU")
entradaA = input("Insira o valor de a: ")
entradaB = input("Insira o valor de b: ")
entradaC = input("Insira o valor de c: ")
b = int(entradaB)
if int(entradaA) == 0:
	print("O Valor de A precisa ser diferente de 0")
delta = pow(b, 2) - (4 * int(entradaA) * int(entradaC))
if delta < 0: 
	print("A equação nao possui raizes reais ")
if delta == 0:
	x1 = ((b * -1) + sqrt(delta)) / (2*int(entradaA))
	print("A equação possui raizes reais repetidas")
	print("A raiz da equação define x = "+str(x1))
if delta > 0:
	x1 = ((b * - 1) + pow(delta, 1/2)) / (2*int(entradaA))
	x2 = ((b * - 1) - pow(delta, 1/2)) / (2*int(entradaA))
	print("As duas raízes da equação são "+str(x1)+" e "+str(x2))