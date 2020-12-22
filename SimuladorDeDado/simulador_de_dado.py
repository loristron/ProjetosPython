import random
import PySimpleGUI as sg

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        # Layout
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('Sim'),sg.Button('Não')]
        ]
    
    def Iniciar(self):
        # criar uma janela
        self.janela = sg.Window('Simulador de Dado',layout=self.layout)
        # ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
        # fazer alguma coisa com esses valores
        try:
            if self.eventos == 'Sim' or self.eventos == 's' or self.eventos == 'S':
                self.GerarValorDoDado()
            elif self.eventos == 'Não' or self.eventos == 'n' or self.eventos == 'N':
                print('Agrecemos a sua participação!')
            else:
                print('S/N')
        except:
            print('Ciao')
    
    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()