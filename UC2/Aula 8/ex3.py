#Ex3 - Utilizando for, faça um programa que peça 5 números ao usuário e no final dê a sua soma
print("Bem-vindo(a), você digitará 5 números!")
soma = 0
for i in range(5):
    numero = int(input("Digite seu número: "))
    soma += numero
print(f"O resultado de cada número digitos é {soma}")