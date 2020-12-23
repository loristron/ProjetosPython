#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, 
#e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
# Média de Aproveitamento  Conceito
#  Entre 9.0 e 10.0        A
#  Entre 7.5 e 9.0         B
#  Entre 6.0 e 7.5         C
#  Entre 4.0 e 6.0         D
#  Entre 4.0 e zero        E

#O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” 
#se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

print("SISTEMA ESCOLAR")
nota1 = input("Insira sua primeira nota: ")
nota2 = input("Insira sua segunda nota: ")

media = (float(nota1) + float(nota2)) / 2

if media >= 9: 
	conceito = "A"
	aprovado = True
if media >= 7.5 and media < 9:
	conceito = "B"
	aprovado = True
if media >= 6 and media < 7.5:
	conceito = "C"
	aprovado = True
if media >= 4 and media < 6:
	conceito = "D"
	aprovado = False
if media < 4:
	conceito = "E"
	aprovado = False

print("NOTAS: "+nota1+" e "+nota2)
print("MÉDIA: "+str(media))
print("CONCEITO: "+conceito)
if aprovado == True:
	print("APROVADO! ")
if aprovado == False:
	print("REPROVADO! ")
