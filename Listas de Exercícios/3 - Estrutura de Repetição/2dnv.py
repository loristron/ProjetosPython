

"""
#Faça um programa que leia um nome de usuário e a sua senha e não aceite 
#a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações."""


valido = False 
while valido == False:  
    usuario = input("login: ")
    senha = input("senha: ")
    if usuario == senha: 
        print("Erro! O login e a senha precisam ser diferentes")
    else: 
        print("Aceito!")
        valido = True

print("fimmmm")


