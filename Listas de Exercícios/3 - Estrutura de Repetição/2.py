#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
#mostrando uma mensagem de erro e voltando a pedir as informações.
aid = True
user = input("Insira um nome de usuário: ")

while aid == True:
	pswd = input("Insira uma senha: ")
	if pswd == user:
		print("A senha não pode ser igual ao nome de usuário! ")
	else: 
		aid = False
print("Usuário criado com sucesso! ")