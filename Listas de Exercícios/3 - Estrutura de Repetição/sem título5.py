
""


"""
Created on Sun Jun 28 11:49:10 2020

@author: loris

Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: 
    
valor da dívida, 
valor dos juros, 
quantidade de parcelas
valor da parcela.

Os juros e a quantidade de parcelas seguem a tabela abaixo:
Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida

1       0
3       10
6       15
9       20
12      25

Exemplo de saída do programa:
    
Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
R$ 1.000,00     0               1                       R$  1.000,00
R$ 1.100,00     100             3                       R$    366,00
R$ 1.150,00     150             6                       R$    191,67

"""

valoresDividas = []
valoresJuros = []
qtdParcelas = []
valorParcela = []


print("Calculadora de Juros")
divida = int(input("Digite o valor da dívida: "))
valoresDividas.append(divida)
print("Valor da Dívida Juros \t Qtd. Parcelas \t Valor Parcela")

for j in range (0, 30, 5):
    valoresJuros.append(j)
        
for n in range(0, 6):   
    valoresDividas.append(valoresDividas[n] +(valoresDividas[n] * valoresJuros[n]/100))

for p in range (0, 13, 3):
    if p == 0:
        qtdParcelas.append(p+1)
    else:
        qtdParcelas.append(p)

for v in range(1, 6):
    parcela = valoresDividas[v] / qtdParcelas[v-1]
    valorParcela.append(round(parcela, 2))   
    
for pri in range(0,5):
    print("R$ "+str(valoresDividas[pri+1])+"\t "+str(valoresJuros[pri])+"%\t "+str(qtdParcelas[pri])+"\t\t R$ "+str(valorParcela[pri]))

