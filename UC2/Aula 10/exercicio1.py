#Exercício 01 - Faça um programa que gera 3 números aleatórios (float)entre 1 e 15 e você tem 1 tentativa para descobrir qual é o maior.

import random

numero1 = random.uniform(1, 15)
numero2 = random.uniform(1, 15)
numero3 = random.uniform(1, 15)

for i in range (1):

    tentativa = int(input(f"Digite Qual tentativa é a mais alta:\nOpção: 1\nOpção: 2\nOpção: 3 \n"))
    if tentativa == 1 and (numero1 > numero2) and (numero1 > numero3):
        print("Parabens, você acertou")
    elif tentativa == 2 and (numero2 > numero1) and (numero2 > numero3):
        print("Parabens, voce acertou!")
    elif tentativa == 3 and (numero3 > numero1) and (numero3 > numero2):
        print("Parabens, voce acertou!")
    else:
        print("Voce errou!")
    print(f"os numeros aleatorios: \n{numero1}, \n{numero2}, \n{numero3}")