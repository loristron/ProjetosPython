#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
#calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

print('TEMPO DE DOWNLOAD')
tamanho = input('\nInsira o tamanho (em MB) do arquivo a ser baixado: ')
velocidade = input('\nInsira a velocidade (em Mbps) da conexão de internet: ')

tempo = float(tamanho) / float (velocidade)
hora = tempo / 60
minutos =( hora - int(hora) ) * 100

print('\nO arquivo será baixado em '+str(round(tempo, 2))+' minutos')
print('\nTempo total de download: '+str(int(hora))+':'+str(int(minutos)))