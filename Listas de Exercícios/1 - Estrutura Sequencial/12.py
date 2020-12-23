#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
#utilizando as seguintes fórmulas:
##Para homens: (72.7*h) - 58
##Para mulheres: (62.1*h) - 44.7

print('\nPeso Mediano por Sexo')
sexo = input('\nVocê é homem(H) ou mulher(M)? ')
altura = input('\nInsira sua altura: ')
if (sexo == 'H' or sexo == 'h'): 
	peso = ((72.7 * float(altura)) - 58)
	print('\nVocê é homem e seu peso ideal é '+str(peso))
elif (sexo == 'M' or sexo == 'm'):
	peso = ((62.1 * float(altura)) - 44.7)
	print('\nVocê é mulher e seu peso ideial é '+str(peso))
