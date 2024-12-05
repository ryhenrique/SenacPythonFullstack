# main.py

from funcoes import calcular_area_retangulo, calcular_fatorial

base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))
area = calcular_area_retangulo(base, altura)
print(f"A área do retângulo é: {area}")

numero = int(input("Digite um número para calcular o fatorial: "))
fatorial = calcular_fatorial(numero)
print(f"O fatorial de {numero} é: {fatorial}")