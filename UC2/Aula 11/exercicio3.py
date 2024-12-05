#Você é um aventureiro carregando uma mochila que comporta 3 itens, atualmente ela tem 3 itens: uma espada, uma poção e um escudo. Ao longo da aventura encontra um arco no chão
#E precisar decidir se o coloca na mochila ou não. Caso coloque, precisará descartar outro item a sua escolha. Faça um programa simulando essa história e decisão usando lista/vetor

print("Você está caminhando pela floresta do Mendanha")
itens = ["espada", "poção", "escudo"]
print(f"Seus itens são: {itens}")
arco_adicional = input("Digite arco para colocar na mochila\n")

if arco_adicional == "arco":

    print("Arco adicionado!\nVocê precisa remover um item do inventário para carrega o arco!")

    remover_item = input("Qual item deseja remover?\n").lower()

    #Verificando se o item existe no iventário
    if remover_item in itens:
        itens.append(arco_adicional)
        itens.remove(remover_item)
        print(f"Você removeu {remover_item} e agora está carregando um arco.")
        print(f"Seus itens final são", itens)
    else:
        print(f"O item '{remover_item} não está no inventário. Nada foi removido.")
else:
    print("Você decidiu não pegar o arco e continuou sua jornada.")

print("História Part 2 - Você segue seu caminho na floresta, um bandido armado surge.")
escolha = int(input("Opção 1: Sacar sua espada\nOpção 2: Entregar sua poção\n"))
if escolha == 1:
    if "espada" in itens:
        print("Você ganhou, segue a sua caminhada!")
    else:
        print("Você estava desarmado e perdeu o jogo!")
elif escolha == 2:
    if "poção" in itens:
        print("Você entregou a poção, segue a sua caminhada!")
    else:
        print("Você não tem poção no inventário, o bandido ficou furioso, fim de jogo!")    
else:
    print("Você não escolheu nenhuma das opções e automaticamente você foi derrotado e perdeu!")
    print("Fim de jogo!")