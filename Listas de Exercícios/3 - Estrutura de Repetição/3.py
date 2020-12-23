#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

nameloop = True
ageloop = True
sLoop = True
sexLoop = True
estCLoop = True

while nameloop == True: 
	nome = input("Insira um nome com três ou mais caracteres: ")
	if len(nome) > 2:
		nameloop = False
	else: 
		print("Entrada Inválida! ")

while ageloop == True:
	idade = input("Insira uma idade entre 0 e 150: ")
	if int(idade) >= 0 and int(idade) < 150:
		ageloop = False
	else:
		print("Entrada inválida! ")
while sLoop == True:
	salario = input("Insira um salário maior que zero: ")
	if int(salario) >= 0:
		sLoop = False
	else:
		print("Insira uma entrada válida! ")
while sexLoop == True:
	sexo = input("Sexo: F-Feminino e M-Masculino: ")
	if sexo == 'f' or sexo == 'F' or sexo == 'm' or sexo == 'M':
		sexLoop = False
	else:
		print("Insira uma entrada Válida! ")
while estCLoop == True: 
	estadoC = input("Estado civil: S-Solteiro; C-Casado, V-Viúvo, D-Divorciado: ")
	s = estadoC.lower()
	if s == 'c' or s == 's' or s == 'v' or s == 'd':
		estCLoop = False
	else:
		print("Insira uma entrada válida! ")

print("Acabou! :) ")