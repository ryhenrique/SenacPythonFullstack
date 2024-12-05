# Função: Calcula o quadrado de um número
def quadrado(numero):
    return numero ** 2

numero = float(input("Digite um número: "))
resultado = quadrado(numero) # Recebe o retorno da função
print(f"O quadrado de {numero} é {resultado}")

#CÓDIGO PRINCIPAL: Pode chamar recursos que estão em outras partes com o objetivo de evitar códigos repetitivos ou redundâncias.
#Funções podem ficar em outros arquivos.py ou dentro do mesmo código