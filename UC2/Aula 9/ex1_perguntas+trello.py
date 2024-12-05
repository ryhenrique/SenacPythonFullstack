pontuação1 = 0
pontuação2 = 0
pontuação3 = 0
soma = 0
resultado = 0
jogarnovamente = True

print("Seja Bem-Vindo ao Kahoot.io/")

while jogarnovamente:
    pergunta1 = input("O criador do Python é Guido Van Rossum? Responda com Verdade ou Falso!\n").lower()
    if pergunta1 == "verdade":
        print("Você acertou a pergunta!")
        pontuação1 += 10
        print(f"Você ganhou: {pontuação1} pontos")
    else:
        print("Você errou a pergunta ou não respondeu!")
        print("É verdade que o Guido Van Rossum é o Criador do Python!")

    pergunta2 = input("O símbolo da Cobra é do Ruby?\n").lower()
    if pergunta2 == "verdade":
        print("Você errou a pergunta!")
    else:
        print("Você acertou a pergunta!")
        pontuação2 += 10
        print(f"Você ganhou: {pontuação2} pontos")

    pergunta3 = input("O Python começou em 1989?\n").lower()
    if pergunta3 == "verdade":
        print("Você acertou a pergunta!")
        pontuação3 += 10
        print(f"Você ganhou: {pontuação3} pontos")
    else:
        print("Você errou a pergunta!")

    soma = pontuação1 + pontuação2 + pontuação3
    print(f"O seu resultado da sua pontuação é: {soma}")

    if soma >= 20:
        print("Você ganhou o jogo!")
    else:
        print("Você perdeu o jogo")

    jogar = input("Deseja jogar novamente? Responda com sim ou não\n").lower()
    if jogar == "sim":
        jogarnovamente = True
    else:
        jogarnovamente = False