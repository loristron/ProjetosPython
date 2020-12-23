#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?" 
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
#Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 
#5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

print("SISTEMA DE POLÍCIA")
print("Respoda as peguntas com 's' para sim e 'n' para não: ")
r1 = input("VocÊ telefonou para a vítima? ")
r2 = input("Esteve no local do crime? ")
r3 = input("Mora perto da vítima? ")
r4 = input("Devia para a vítima? ")
r5 = input("Já trabalhou com a vítima? ")
contador = 0
if r1 == 's':
	contador += 1
if r2 == 's':
	contador += 1
if r3 == 's':
	contador += 1
if r4 == 's':
	contador += 1
if r5 == 's':
	contador += 1
if contador == 2:
	print("Você é suspeito do crime. ")
if contador > 2 and contador <= 4:
	print("Você foi considerado cúmplice")
if contador == 5:
	print("Você é o Assassino! ")
if contador == 1:
	print("Você é inocente =) ") 
