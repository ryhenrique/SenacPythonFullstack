# Faça um programa que simule o armário de uma escola e permita colocar o nome do aluno responsável/pagante da gaveta. O armário tem a dimensão 5x5.
matriz1 = [
    ["", "", "", "", ""],
    ["", "", "", "", ""],
    ["", "", "", "", ""],
    ["", "", "", "", ""],
    ["", "", "", "", ""]
    
]

#A escola adicionou um novo armario 3x3 perto das salas de aula e o chamou de armário vip. Caso o aluno adquira uma gaveta no armário comum, custará R$30,00 ao mês.
#O vip custará R$50,00. Adicione no sistema essa seleção e retorne para o usuário o custo.
    
matriz2 = [
    ["", "", "",],
    ["", "", "",],
    ["", "", "",],
    
]

valortotal = 0

print("Bem-Vindo ao Sistema de Armários Escolar")
nome = input("Qual é o seu nome?\n")
armario = int(input("Opção 1 - Armário comum\nOpção 2 - Armário Vip\n"))

if armario == 1:
    valortotal = 30
    print(f"Você escolheu o Armário Comum!")
    linha = int(input("Em qual linha do armário você deseja colocar o seu nome? (0 e 4)\n"))
    coluna = int(input("Em qual coluna do armário será a sua gaveta? (0 a 4)\n"))
    matriz1[linha][coluna] = nome
    for linha in matriz1:
        print(linha)
    print(f"A sua seleção foi escolhida e seu custo foi R$ {valortotal}")

elif armario == 2:
    valortotal = 50
    print(f"Você escolheu o Armário Vip")
    linha = int(input("Em qual linha do armário você deseja colocar o seu nome? (0 a 2)\n"))
    coluna = int(input("Em qual coluna do armário será a sua gaveta? (0 a 2)\n"))
    matriz2[linha][coluna] = nome
    for linha in matriz2:
        print(linha)
    print(f"A sua seleção foi escolhida e seu custo foi R$: {valortotal}")
else:
    print("O dia que quiser comprar o armário, fale com conosco na secretaria!")