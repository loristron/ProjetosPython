#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.

print("Celsius para Farenheit")
C = input("\nInsira o valor em Celsius: ")
F = (int(C) * (9/5) + 32)
print ("\n"+str(C)+" Celsius = "+str(F)+" Farenheit")
