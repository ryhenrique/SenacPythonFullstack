#Faça um programa que conte de 0 a 10 e diga no final "Obrigado por esperar! estamos redirecionando sua ligação"

import time
print("Iniciando a contagem regressiva!")
contador = 0

while contador < 11:
    print(contador)
    time.sleep(1)
    contador += 1

print("Obrigado por esperar! Estamos redirecionando a sua ligação")