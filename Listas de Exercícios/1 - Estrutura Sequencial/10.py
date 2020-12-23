#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
##o produto do dobro do primeiro com metade do segundo . PRODUTO = resultado de uma multiplicação
##a soma do triplo do primeiro com o terceiro.
##o terceiro elevado ao cubo.

print("Inteiros e reais")
i1 = input("\nInsira um número inteiro: ")
i2 = input("\nInsira um segundo numero inteiro: ")
r1 = input("\nInsira um número real: ")

produto = (int(i1) * 2 ) * (int(i2)/2) 
soma = (int(i1)*3) + float(r1)
cubo = pow(float(r1), 3)

print('\nProduto do dobro do primeiro com metade do segundo: '+str(produto))
print('\nSoma do triplo do primeiro com o terceiro: '+str(soma))
print("\nTerceiro elevado ao cubo: "+str(cubo))