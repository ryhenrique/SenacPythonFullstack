
import random

numero = random.randint(1, 200)

print("Qual o nível de dificuldade você gostaria de jogar?")
print("1 - Fácil (10 tentativas)")
print("2 - Médio (7 tentativas)")
print("3 - Difícil (5 tentativas)")

nivel = input("Escolha o nível de dificuldade (1, 2 ou 3): ")

if nivel == '1':
    tentativas = 10
elif nivel == '2':
    tentativas = 7
elif nivel == '3':
    tentativas = 5
else:
    print("Nível inválido")
    exit()
for tentativa in range(1, tentativas + 1):
    palpite = int(input(f"Tentativa {tentativa}: Adivinhe o número (entre 1 e 200): "))
    if palpite == numero:
        print("Parabéns! Você acertou o número!")
        break
    elif palpite < numero:
        print("O número é maior.")
    else:
        print("O número é menor.")
else:
    print(f"Você não conseguiu adivinhar o número em {tentativas} tentativas. O número era {numero}.")
