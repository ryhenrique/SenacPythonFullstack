import random

#Gerando 4 números aleatórios e armazenando em uma lista
numeros = {random.randint(20,50) for i in range(4)}

#Exibindo os números gerados
print(f"Números gerados: {numeros}")

#Ordenando os números com a função sort
numeros.sort()
numeros.reverse()

print(f"Números ordenados: {numeros}")