#main.py
from calculadora import somar, subtrair, multiplicar, dividir

print("Selecione a operação:")
print("1 Somar")
print("2 Subtrair")
print("3 Multiplicar")
print("4 Dividir")

escolha = input("")

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if escolha == '1':
    resultado = somar(numero1, numero2)
    print(resultado)
elif escolha == '2':
    resultado = subtrair(numero1, numero2)
    print(resultado)
elif escolha == '3':
    resultado = multiplicar(numero1, numero2)
    print(resultado)
elif escolha == '4':
    resultado = dividir(numero1, numero2)
    print(resultado)
else:
    print("Opção inválida.")