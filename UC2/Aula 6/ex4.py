#Faça um programa que peça 1 número ao cliente e faça sua tabuada (até ao 10)

x = 1
multiplica = 1

numero = int(input("Entre com um número para multiplicar até ao 10: "))

while x < 11:    
    multiplica = numero * x
    print(f"A sua multiplicação é {numero}x{x} = {multiplica}")
    x += 1