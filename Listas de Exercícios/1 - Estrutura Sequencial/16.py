#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
#Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
#que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

print('LOJA DE TINTA TUNADA')
area = input('\nInsira o tamanho em metros da área a ser pintada: ')

litros = float(area) / 6
latas = litros / 18
barril = litros / 3.6
precoLatas = round(latas+0.5) * 80
preçoBarril = round(barril+0.5) * 25

print('\nOrçamento para cobrir '+str(float(area))+'m2')
print('\n - LATAS: '+str(round(latas+0.5))+' por R$'+str(precoLatas))
print('\n - BARRIL: '+str(round(barril+0.5))+' por R$'+str(preçoBarril))