#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
#Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 

#11% para o Imposto de Renda, 
#8% para o INSS e 
#5% para o sindicato

#Faça um programa que nos dê:
##salário bruto.
##quanto pagou ao INSS.
##quanto pagou ao sindicato.
##o salário líquido.
##calcule os descontos e o salário líquido, conforme a tabela abaixo:
##+ Salário Bruto : R$
##- IR (11%) : R$
##- INSS (8%) : R$
##- Sindicato ( 5%) : R$
##= Salário Liquido : R$
#Obs.: Salário Bruto - Descontos = Salário Líquido.

print ('CONTRACHEQUE')

valorHora = input('\nQuanto você ganha por hora? R$')
horasMes = input('\nQuantas horas você trabalha, em um mês? ')

salarioBruto = float(valorHora) * float(horasMes)

IR = salarioBruto * 0.11
INSS = salarioBruto * 0.08
SIND = salarioBruto * 0.05

salarioLiquido = salarioBruto - IR - INSS - SIND

print('\n+ Salário Bruto : R$'+str(salarioBruto))
print('\n- IR (11%) : R$'+str(IR))
print('\n- INSS (8%) : R$'+str(INSS))
print('\n- Sindicato (5%) : R$'+str(SIND))
print('\n= Salário Liquido : R$'+str(salarioLiquido))

