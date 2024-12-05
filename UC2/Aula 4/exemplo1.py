#if = Se - (Primeira Condicional) 
#elif = Demais Condicionais
#else = Caso ao contrário ou então (Ocorre quando nenhuma condição dos elif ou if for atendida)
#and = e

#Exemplo 1 - Eu sou obrigado a votar?

idade = int(input("Qual a sua idade?"))

if (idade>=18 and idade<=65):
    print("Sim você é obrigado a votar")
else:
    print("Não, você não é obrigado a votar")