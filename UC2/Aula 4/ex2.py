# Simbolos em Tabela
# sinal > maior
# sinal < menor
# sinal >= maior ou igual
# sinal <= menor ou igual
# sinal == igual
# != Diferente

# Exercício 2 - Faça um programa que pergunte quantas rodas tem um veiculo, se tiver 4 diga que é um carro ou van
rodas = int(input("Quantas rodas tem um veículo?"))

if (rodas==4):
    print("Essa quantidade de rodas, é um carro ou uma van")
elif (rodas == 2):
    print("O veículo é uma moto ou bicleta")
elif (rodas == 1):
    print("O veículo é um monociclo")

elif (rodas == 6):
    print("O veículo é um ônibus")

elif(rodas>=8 and rodas<=20):
    print("Esse veículo provavelmente será um caminhão")

else:
    print("Esse veículo não foi encontrado com essa quantidade de rodas!")