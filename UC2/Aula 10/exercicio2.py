#Faça um programa que gera 4 números aleatórios entre 20 e 50 e depois os ordena de forma decrescente

import random

numero1 = random.randint(20, 50)
numero2 = random.randint(20, 50)
numero3 = random.randint(20, 50)
numero4 = random.randint(20, 50)

print(f"{numero1} {numero2} {numero3} {numero4}")

if numero1 > numero2:
    numero1, numero2 = numero2, numero1
if numero1 > numero3:
    numero1, numero3 = numero3, numero1
if numero1 > numero4:
    numero1, numero4 = numero4, numero1
if numero2 > numero1:
    numero2, numero1 = numero1, numero2
if numero2 > numero3:
    numero2, numero3 = numero3, numero2
if numero2 > numero4:
    numero2, numero4 = numero4, numero2
if numero3 > numero1:
    numero3, numero1 = numero1, numero3
if numero3 > numero2:
    numero3, numero2 = numero2, numero3
if numero3 > numero4:
    numero3, numero4 = numero4, numero3
if numero4 > numero1:
    numero4, numero1 = numero1, numero4
if numero4 > numero2:
    numero4, numero2 = numero2, numero4
if numero4 > numero3:
    numero4, numero3 = numero3, numero4

print(f"Os números ordenados decrescententemente são: {numero1}, {numero2}, {numero3:} e {numero4:}")