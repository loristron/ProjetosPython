#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

print('Bimestrais')
print('\nInsira o valor das duas quatro notas bimestrais')
p1 = input('\nNota 1: ')
p2 = input('\nNota 2: ')
p3 = input('\nNota 3: ')
p4 = input('\nNota 4: ')

media = (int(p1) + int(p2) + int(p3) + int(p4))/4
print('\nSua média Bimestral foi de '+str(media))