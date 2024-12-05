#Exercicio de treinamento do aventureiro:
import time
aventureiro = [
    ["Vida", "Ataque"],
    [100, 20]
]
for linha in aventureiro:
    print(linha)
print("o treino começou!")
while  aventureiro[1][1] < 30:
    aventureiro[1][1] += 1
    print("o poder de ataque atual é", aventureiro[1][1])
    time.sleep(7)
print("Status final:")
for linha in aventureiro:
    print(linha)