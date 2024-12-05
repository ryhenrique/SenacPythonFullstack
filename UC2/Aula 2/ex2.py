#Crie um programa que pergunte o nome do cliente o modelo do carro, a cor do carro, e imprima uma mensagem agradecendo a preferência com as informações solicitadas ao cliente na mensagem

nome_do_cliente = input("Qual seu nome?")
modelo_do_carro = input("Qual o modelo do carro?")
cor_do_carro = input("Qual a cor do do carro?")

#Imprindo as variáveis

print(nome_do_cliente)
print(modelo_do_carro)
print(cor_do_carro)

#Mensagem de agradecimento
print("Muito obrigado pela preferência!")

#Pergunte se gostaria que a Lavagem do Carro seja realizada hoje ou amanhã!
print("Gostaria que a lavagem fosse realizada hoje ou amanhã?")
resposta = input( )
print(f"A limpeza do {modelo_do_carro} será realizado {resposta}")