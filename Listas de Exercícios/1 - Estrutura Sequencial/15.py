#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
#A cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros que custam R$ 80,00. 
#Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
print('LOJA DE TINTAS')
area = input("\nInsira a area a ser pintada, em m2: ")
litros  = float(area) / 3
latas = litros / 18
preco = round(latas+0.5) * 80	
roundLatas = round(latas+0.5)
print("Para cobrir "+str(float(area))+"m2, você precisará de "+str(roundLatas)+" latas de tinta e pagará R$"+str(preco))