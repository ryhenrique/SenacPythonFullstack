#Contador += 1 mesma coisa de Contador = Contador+1
#Contador -= mesma coisa
#Contador = contador - 1


import time
print("inciando contagem regressiva")
contador = 5

while contador > 0:
    print(contador)
    time.sleep(1)
    contador -= 1

print("Fim da contagem regressiva! Boom")