import random

#Simula o lançamento de uma moeda
resultado = "Cara" if random.randint(0, 1) == 0 else "Coroa"
print(f"O resultado do lançamento da moeda é: {resultado}")