#Faça um programa para o cálculo de uma folha de pagamento, 
#sabendo que os descontos são do Imposto de Renda, 
#que depende do salário bruto (conforme tabela abaixo) 
#e 10% para o INSS e que o FGTS corresponde a 11% do 
#Salário Bruto, mas não é descontado (é a empresa que deposita)
#O Salário Líquido corresponde ao Salário Bruto menos os
# descontos. O programa deverá pedir ao usuário o valor da sua
# hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% 
#Imprima na  tela as informações, dispostas conforme o exemplo
#abaixo. 
#No exemplo o valor da hora é 5 e a quantidade de hora é
#220.

print("FOLHA DE PAGAMENTO")
entradaHora = input("Insira a quantidade de horas trabalhadas por mês: ")
entradaValor = input("Insira o valor de cada hora trabalhada: R$")
salarioBruto = float(entradaHora) * float(entradaValor)
INSS = salarioBruto * 0.1
FGTS = salarioBruto * 0.11
if salarioBruto <= 900:
	IR = 0
if salarioBruto <= 1500:
	IR = 0.05
if salarioBruto <= 2500:
	IR = 0.1
if salarioBruto > 2500:
	IR = 0.2
descontoIR = salarioBruto * IR
salarioLiquido = salarioBruto - descontoIR - INSS
print("\nSalário Bruto: ("+entradaHora+" * "+entradaValor+") \t: R$ "+str(salarioBruto))
print("(-) IR ("+str(IR*100)+"%)\t\t\t\t : R$ "+str(salarioBruto*IR))
print("(-) INSS (10%) \t\t\t\t : R$ "+str(INSS))
print("FGTS (11%) \t\t\t\t\t : R$ "+str(FGTS))
print("Total de descontos: \t\t : R$ "+str(descontoIR + INSS))
print("Salário Liquido\t\t\t\t:   R$ "+str(salarioLiquido))