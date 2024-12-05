#Faça um programa que: Pergunte se o usuário quer um combo ou 1 item individual. Onde:
#1° Hamburguer custa R$10.00
#2° Batata frita custa R$10.00
#3° Refrigerante custa R$10.00
#4° O combo custa R$22.00
#O cliente pode adicionar 2 itens, mas caso faça, ofereça o 3° item, por R$2,00, incentivando e vendendo indiretamente o combo

print("Bem-vindo ao Mc Donalds!")
item = int(input("Digite 1 para combo \nDigite 2 para o item individual! \n"))    
if (item == 1):
    lanche = "Combo!"
    print(f"Você selecionou o {lanche}")

elif (item == 2):
    lanche = "item individual!"
    print(f"Você selecionou o {lanche}")

else:
    print("Teste")

OpçõesLanche = (input("Deseja ver as opções de lanche?\n 1 - Sim!\n 2 - Não!\n" ))
if (OpçõesLanche == 1 ):
    print("Hambúrguer R$10,00\n Batata frita R$10,00\nRefrigerante R$10,00")