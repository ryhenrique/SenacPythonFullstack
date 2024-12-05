#Faça um programa que diga quais dos 20 primeiros multiplos de 5 são pares

soma = 0

for i in range(5, 101, 5):
    if i % 2 == 0:
        print(i)

    if i % 2 != 0:
        soma += i
print(f"A soma dos números ímpares é: {soma}")