#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o 
#programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
##salários até R$ 280,00 (incluindo) : aumento de 20%
##salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
##salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
##salários de R$ 1500,00 em diante : aumento de 5% 

#Após o aumento ser realizado, informe na tela:
##o salário antes do reajuste;
##o percentual de aumento aplicado;
##o valor do aumento;
##o novo salário, após o aumento.

print("REAJUSTE SALARIAL")
entrada = input("Insira seu salário: R$")
salario = float(entrada)

if salario <= 280:
	reajuste = "5%"
	aumento = (salario * 0.2)
	novoSalario =  aumento + salario
if salario > 280 and salario <= 700:
	reajuste = "15%"
	aumento = (salario * 0.15)
	novoSalario =  aumento + salario
if salario > 700 and salario <= 1500:
	reajuste = "10%"
	aumento = (salario * 0.1)
	novoSalario =  aumento + salario
if salario > 1500:
	reajuste = "5%"
	aumento = (salario * 0.05)
	novoSalario =  aumento + salario
print("\nSALÁRIO ANTERIOR AO REAJUSTE: R$"+str(salario))
print("REAJUSTE APLICADO: "+reajuste)
print("VALOR DO AUMENTO: R$"+str(round(aumento, 2)))
print("NOVO SALÁRIO: R$"+str(novoSalario))