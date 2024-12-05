#Jogo do palpite. O sistema gera 1 numero aleatorio entre 1 e 200. O usuário tem 10 palpites para tentar acertar.
#O sistema sempre dá um feedback dizendo se o "numero secreto" é maior ou menor que o palpite do usuário

import random

numero_aleatorio = random.randint(1, 200)
print("Essa é sua primeira tentativa!")
for i in range(10):
    palpite = int(input("Digite o seu palpite: "))
    if palpite > numero_aleatorio:
        print("O seu numero é maior que o numero secreto")
    elif palpite < numero_aleatorio:
        print("O seu numero é menor que o numero secreto")
    else:
        print("Parabéns você acertou o palpite!")
else:
    print(f"O numero era: {numero_aleatorio}")