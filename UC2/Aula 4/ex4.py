#Exercício 4 - Faça um programa que diga se um número é par ou impar #Dica: Para pegar o resto de uma divisão, utilize "%"
#Exemplo: O resto da divisão de 6 por 3 é 0. 6%3 = 0 o resto da divisão de 4 por 3 é 1. 4%3 = 1

print("Seja bem-vindo ao sistema de números pares e ímpares!")
numero = int(input("Digite um número para a divisão:"))

if (numero % 2 == 0 ):
    print("Esse número é par")

else:
    print("Esse número é impar")