#Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
#C = (5 * (F-32) / 9)

print("Farenheit para Celsius")
F = input("\nInsira valor em Farenheit: ")
C = (5 * (float(F) - 32) / 9)
print("\n"+str(F)+" Farenheit = "+str(C)+" graus Celsius")