#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

print('Calculando a área de um círculo')
r = input('\nInsira o raio do círculo: ')
a = pow(float(r), 2) * 3.1415
print('A área do círculo é '+str(a))