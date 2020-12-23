#Faça um Programa que verifique se uma letra digitada é 
#vogal ou consoante.

print("VOGAL OU CONSOANTE? ")
entrada = input("Insira uma letra: ")

vogais = 'aeiou'
consoates = 'bcdfghjklmnopqrstvwxyz'

vc = len(consoates)
vv = len(vogais)

if (entrada in vogais) == True:
	print("Você digitou uma vogal")
if (entrada in vogais) == False:
	print("Você digitou uma consoante")
