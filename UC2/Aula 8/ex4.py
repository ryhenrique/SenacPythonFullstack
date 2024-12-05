#Ex 4: Faça um programa usando for que peça 4 números e some apenas os números ímpares

resultado = 0
for i in range(4):
    numero = int(input("Digite o número: "))
    if numero % 2 != 0:
        resultado += numero
print(f"O resultado da sua soma é: {resultado}")