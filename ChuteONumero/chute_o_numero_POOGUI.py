import random
import PySimpleGUI as sg

class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_min = 1
        self.valor_max = 100
        self.tentar_novamente = True
    
    def Iniciar(self):
        #elementos do layout
        layout = [
            [sg.Text("Digite seu chute: ", size=(20,0))],
            [sg.Input(size=(18,0), key='ValorChute')],
            [sg.Button('Chutar!')],
            [sg.Output(size=(40,10))]
        ]
        #criação da janela
        self.janela = sg.Window("Chute um Número!", layout=layout)
        self.GerarNumeroAleatorio()
        try:
            while True:
                #leitura dos valores da tela
                self.evento, self.valores = self.janela.Read()
                #Tratamento dos Valores Lidos
                if self.evento == 'Chutar!':
                    self.valor_chute = self.valores['ValorChute']
                    while self.tentar_novamente == True:
                        if int(self.valor_chute) < self.valor_aleatorio:
                            print("Chute um valor mais alto!")
                            break
                        elif int(self.valor_chute) > self.valor_aleatorio:
                            print("Chute um valor mais baixo!")
                            break
                        elif int(self.valor_chute) == self.valor_aleatorio:
                            self.tentar_novamente = False
                            print("Acertou!! O numero correto era "+str(self.valor_aleatorio))
                            break
        except:
            print("Aconteceu um erro.")
            self.Iniciar()


    def GerarNumeroAleatorio(self):    
        self.valor_aleatorio = random.randint(self.valor_min, self.valor_max)

chte = ChuteONumero()
chte.Iniciar()