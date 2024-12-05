#Após a aventura da aula passada, o aventureiro resolveu treinar mais seu combate: faça uma simulação onde o aventureiro tem uma lista [100, 20], onde 100 é a vida dele e 20 é o poder de ataque dele, e a cada 7 segundos de treino, ele aumenta o seu poder de ataque em 1 com o limite máximo de 30 para o seu poder ataque

vida = [100]
poder = [20]

import time

print("Contagem para o aumento de poder!")
poder = 20

while poder <= 29:
    print(poder)
    time.sleep(7)
    poder += 1
    print(f"Você atingiu o limite máximo de: {poder}")
print(f"Sua vida atual é {vida} e seu poder é {poder}")