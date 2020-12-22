import random as rd

def main():
    resposta = rd.randint(0, 100)
    print(resposta)
    acerto = False
    while acerto == False:
        tentativa = int(input("\nTente acertar o numero que pensei: "))
        if tentativa == resposta:
            print("Parabéns, você acertou!! ")
            acerto = True
        else:
            print("Errou! Tente novamente")

if __name__ == "__main__":
    main()