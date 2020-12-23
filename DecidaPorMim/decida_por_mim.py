#Faça uma pergunta e o programa te dará uma resposta

import random as rd
import PySimpleGUI as sg

class Decisao:
    def __init__(self):
        self.respostas = ["Sim", "Não", "Talvez", "Que pergunta é essa?!", "Talvez na próxima vida", "Nem a pau", "Jamé", "Demais da conta", "Com certeza!", "Prefiro não comentar.", "Tá doido"]
    
    def Iniciar(self):  
        layout = [
            [sg.Text("Faça sua pergunta:")],
            [sg.Input(size=(40,0), key="campo")],
            [sg.Button("Vai!")],
            [sg.Output(size=(40,0))]
        ]
        self.janela = sg.Window("Vamo conversar", layout=layout)
        try:
            while True:
                self.eventos, self.valores = self.janela.Read()
                if self.eventos == 'Vai!':
                    print(rd.choice(self.respostas))
        except:
            print("Deu erro!")

dec = Decisao()
dec.Iniciar()