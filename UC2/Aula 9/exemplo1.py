import random

#Gera um número inteiro aleatório entre 1 e 100

numero_aleatorio = random.randint(1, 100)
print(f"Numero inteiro aleatório entre 1 e 100: {numero_aleatorio}")
print("Entre com dois numeros, irei retornar um numero aleatorio entre eles")
numero_usuario_menor = int(input("Entre com o menor deles: "))
numero_usuario_maior = int(input("Entre com o maior deles: "))
numero_aleatorio2 = random.randint(numero_usuario_menor, numero_usuario_maior)

print(f"Numero inteiro aleatório entre {numero_usuario_menor} e {numero_usuario_maior}:{numero_aleatorio2}")

#Em funções passamos parâmetros(números, variáveis). muitas vezes não temos acesso a lógicapor trás.
#Elas servem para facilitar o desenvolvimento e evitar códigos desnecessários ou "a re-nvenção da roda".
#Bibliotecas constumar ter várias funções