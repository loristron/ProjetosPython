import random

class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_min = 1
        self.valor_max = 100
        self.tentar_novamente = True
    
    def Iniciar(self):
        self.GerarNumeroAleatorio()
        self.PedirValor()
        try:
            while self.tentar_novamente == True:
                if self.valor_chute > self.valor_aleatorio:
                    print("Chute um valor mais baixo!")
                    self.PedirValor()
                elif self.valor_chute < self.valor_aleatorio:
                    print("Chute um valor mais alto!")
                    self.PedirValor()
                elif self.valor_chute == self.valor_aleatorio:
                    self.tentar_novamente = False
                    print("Acertou!! O numero correto era "+str(self.valor_aleatorio))
        except:
            print("Favor digitar apenas numeros inteiros. O programa será reiniciado.")
            self.Iniciar()

    def GerarNumeroAleatorio(self):    
        self.valor_aleatorio = random.randint(self.valor_min, self.valor_max)

    def PedirValor(self):
        self.valor_chute = int(input("Chute um numero: "))

chte = ChuteONumero()
chte.Iniciar()