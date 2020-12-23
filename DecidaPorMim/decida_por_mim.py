#Faça uma pergunta e o programa te dará uma resposta

import random as rd
import PySimpleGUI as sg

class Decisao:
    def __init__(self):
        self.respostas = ["Sim", "Não", "Talvez", "Que pergunta é essa?!", "Talvez na próxima vida", "Nem a pau", "Jamé", "Demais da conta", "Com certeza!", "Prefiro não comentar.", "Tá doido"]
        self.rodando = True

    def Iniciar(self):  
        layout = [
            [sg.Text("Faça sua pergunta:")],
            [sg.Input(size=(40,0), key="campo")],
            [sg.Button("Vai!")],
            [sg.Output(size=(40,0))],
            [sg.Button("Sair")]
        ]
        self.janela = sg.Window("Vamo conversar", layout=layout)
        try:
            while self.rodando == True:
                self.eventos, self.valores = self.janela.Read()
                if self.eventos == 'Vai!':
                    print(rd.choice(self.respostas))
                if self.eventos == 'Sair':
                    self.rodando = False
                    self.janela.Close()
        except:
            print("Deu erro!")

dec = Decisao()
dec.Iniciar()