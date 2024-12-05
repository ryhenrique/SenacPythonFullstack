#Exemplo0
import random

# Configurações do jogo
tamanho_tabuleiro = 5
navio_linha = random.randint(0, tamanho_tabuleiro - 1)
navio_coluna = random.randint(0, tamanho_tabuleiro - 1)

# Inicializa o tabuleiro
tabuleiro = [["~"] * tamanho_tabuleiro for _ in range(tamanho_tabuleiro)]

def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(linha))

# Jogo
tentativas = 4
for tentativa in range(tentativas):
    print(f"\nTentativa {tentativa + 1} de {tentativas}")
    mostrar_tabuleiro(tabuleiro)

    linha = int(input("Adivinhe a linha (0 a 4): "))
    coluna = int(input("Adivinhe a coluna (0 a 4): "))

    if linha == navio_linha and coluna == navio_coluna:
        print("Parabéns! Você afundou o navio!")
        break
    else:
        if linha < 0 or linha >= tamanho_tabuleiro or coluna < 0 or coluna >= tamanho_tabuleiro:
            print("Coordernadas fora do tabuleiro.")
        elif tabuleiro[linha][coluna] == "X":
            print("Você já tentou essa coordenada.")
        else:
            print("Água!")
            tabuleiro[linha][coluna] = "X"

    if tentativa == tentativas - 1:
        print(f"Fim de jogo! O navio estava em ({navio_linha}, {navio_coluna}).")

mostrar_tabuleiro(tabuleiro)
