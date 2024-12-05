#Saudação
print("Olá bem-vindo ao lava jato Senac!")
#Recebendo valores personalizados nas variaveis
nome = input("Digite o seu nome:")
modelodocarro = input("Digite o modelo do seu carro:")
cordocarro = input("Digite a cor do seu carro:")
#Mensagem de agradecimento e confirmação
print("Obrigado pela preferência "+ nome +" o seu veículo:" +modelodocarro + " de cor " + cordocarro + " será limpo em breve")
print("Gostaria que seu veículo "+modelodocarro+" fosse lavado hoje ou amanhã?")
agendamento = input()
print(f"A limpeza do {modelodocarro} será realizado {agendamento}")