#while = Enquanto
#Enquanto uma condição for verdadeira, o código "dentro" dele irá executar. Podemos chamar isso de loop! =
#Aviso: Cuidado com loops infinitos!
#Ctrl + C = Interrompe a execução do código!


soma = 0
contador = 0

#Solicita ao usuário que insira 5 números
while contador < 5:
    numero = float(input("Insira um número: "))
    soma += numero
    contador += 1

# Exibe a soma total
print(f"A soma total é: {soma}")