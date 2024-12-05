#Desenvolva um programa que simula um sistema de reciclagem com contagem dos materiais reciclado. Programa deve:
#Exibir uma mensagem de boas vindas ao usuario : "Bem vindo ao programa de reciclagem! ".

#solicitar ao usuario que informe o tipo de material que ele deseja reciclar, 
# entre vidro, metal, organico ou residuo não reciclavel.

#Com base no material informado, o programa deve informar a cor da lixeira correta para descarte e contabilizar
#a quantidade de cada matereial reciclado: 
#Papel: lixeira azul
#Plastico: lixeira vermelha
#Vidro: lixeira verde
#Metal: lixeira amarela
#Organico: lixeira marrom
#não reciclavel: lixeira cinza
#se nao for reconhecido, exibir a mensagem:"Erro tente novamente" não contabilizar na contagem de nenhuma lixeira.
#Perguntar ao usuario se ele deseja continuar reciclando. se o usuario digitar "s" 
#Programa deve repetir o processo; caso contrario o programa deve exibir um resumo da reciclagem
#com a quantidade de materiais reciclados e a mensagem : "Obrigado por contribuir com a Reciclagem "

nome = input("Qual é o seu nome? \n")
print(f"Bem vindo {nome} ao programa de reciclagem! \n")
print("Temos objetivo de recolher todo material reciclavél e não reciclavél, desse forma contribuímos com a natureza: \n")
papel = 0 
plastico = 0
vidro = 0
metal = 0
organico = 0
nao_reciclavel = 0
n2 = "sim"
while n2 == "sim":
    n1 = int(input(" Qual material deseja descartar? \n\n  1 = Papel: \n  2 = Plastico: \n  3 = Vidro: \n  4 = Metal: \n  5 = Organico: \n  6 = Não reciclavél: \n"))
    if(n1 == 1):
        print(" Coloque na Lixeira Azul ")
        papel = papel + 1
    elif(n1 == 2):
        print("Coloque na lixeira vermelha ")
        plastico = plastico + 1
    elif(n1 == 3):
        print("Coloque na lixeira Verde ")
        vidro = vidro + 1
    elif(n1 == 4):
        print("Coloque na lixeira amarela ")
        metal = metal + 1
    elif(n1 == 5):
        print("Coloque na lixeira Marron ")
        organico = organico +1
    elif(n1 == 6):
        print("Coloque na lixeira cinza ")
        nao_reciclavel = nao_reciclavel + 1
    else:
        print("Erro tente novamente ")
    n2 = input("Gostaria de continuar com a reciclagem? sim ou nao \n").lower()
print(f"O resultado da sua reciclagem foi:\n Papel:{papel}\n Plástico:{plastico}\n Vidro:{vidro}\n Metal:{metal}\n Organico:{organico}\n não reciclavél:{nao_reciclavel}\n ")
print("Obrigado por contribuir com a Reciclagem \n")