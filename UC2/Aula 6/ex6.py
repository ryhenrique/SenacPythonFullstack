#Faça um programa que peça 2 numeros e faça uma operação com base no seguinte menu:
# 1 - Soma
# 2 - Subtrai
# 3 - Multiplica
# 4 - Dividir
soma = 0

numero1 = int(input("Digite o seu 1° número: "))
numero2 = int(input("Digite o seu 2° número: "))

menu = int(input("Digite 1 para Somar\nDigite 2 para Subtrair\nDigite 3 para Multiplicar\nDigite 4 para Dividir\n "))
if menu == 1:
    resultado = numero1 + numero2
    print(f"Essa é a sua soma: {resultado}")
    
elif menu == 2:
    resultado = numero1 - numero2
    print(f"Essa é a sua subtração: {resultado}")

elif menu == 3:
    resultado = numero1 * numero2
    print(f"Essa é a sua multiplicação: {resultado}")

elif menu == 4:
    resultado = numero1 / numero2
    print(f"Essa é a sua divisão: {resultado}")

print(f"Obrigado por utilizar o nosso menu de operações matemáticas - SENAC RJ!")