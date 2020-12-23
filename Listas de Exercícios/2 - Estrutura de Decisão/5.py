#Faça um programa para a leitura de duas notas parciais 
#de um aluno. O programa deve calcular a média alcançada 
#por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou
# igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for 
#igual a dez.

print("NOTAS PARCIAIS")
nota1 = input("Insira sua primeira nota: ")
nota2 = input("Insira sua segunda nota: ")

media = (float(nota1) + float (nota2)) / 2

if media >= 7:
	print("Aprovado")
if media < 7:
	print("Reprovado")
if media == 10:
	print("Aprovado com Distinção")