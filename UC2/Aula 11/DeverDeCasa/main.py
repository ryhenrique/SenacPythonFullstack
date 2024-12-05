from funcoes import soma, subtração, multiplicação, divisão


print("Bem-vindo(a) a Calculadora Básica - SENAC BARRA DA TIJUCA RJ")
print("Digite a numeração da sua escolha: ")

escolha = input("Opção 1: Soma\nOpção 2: Subtração\nOpção 3: Multiplicação\nOpção 4: Divisão\n")
if escolha == "1":
    
    numero1 = float(input("Digite seu 1° numero: "))
    numero2 = float(input("Digite o seu 2° numero: "))
    resultado = soma(numero1, numero2)
    print(f"A soma de {numero1} + {numero2} é = {resultado}")
    
elif escolha == "2":
    
    numero1 = float(input("Digite seu 1° numero: "))
    numero2 = float(input("Digite o seu 2° numero: "))
    resultado = subtração(numero1, numero2)
    print(f"A subtração de {numero1} - {numero2} é = {resultado}")

elif escolha == "3":
    
    numero1 = float(input("Digite seu 1° numero: "))
    numero2 = float(input("Digite o seu 2° numero: "))
    resultado = multiplicação(numero1, numero2)
    print(f"A multiplicação de {numero1} x {numero2} é = {resultado}")

elif escolha == "4":
   
    numero1 = float(input("Digite seu 1° numero: "))
    numero2 = float(input("Digite o seu 2° numero: "))
    resultado = divisão(numero1, numero2)
    print(f"A divisão de {numero1} / {numero2} é = {resultado}")

else:
    print("Você não escolheu nenhuma das opções, tente novamente!")