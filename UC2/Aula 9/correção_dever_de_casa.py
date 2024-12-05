#Programa para mostrar os 10 primeiros números da sequência de Fibonacci

numero1  = 1
numero2 = 1

print(numero1)
print(numero2)

for i in range(8):
    proximo = numero1 + numero2
    print(proximo)
    numero1 = numero2
    numero2 = proximo