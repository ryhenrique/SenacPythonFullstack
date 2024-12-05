# main.py

from minhas_funcoes import cumprimentar, somar

# Usando a função cumprimentar
cumprimentar()

# Usando a função somar
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
resultado = somar(numero1, numero2)
print(f"A soma de {numero1} e {numero2} é {resultado}.")