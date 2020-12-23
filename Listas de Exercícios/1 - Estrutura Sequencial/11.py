#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
#usando a seguinte fórmula: (72.7*altura) - 58
print("Peso 'Ideal'")
altura = input("\nInsira sua altura: ")
pesoI = (72.7 * float(altura)) - 58
print("\nO peso médio para sua altura é de "+str(pesoI))