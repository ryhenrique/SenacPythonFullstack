#Você é um aventureiro carregando uma mochila que comporta 3 itens, atualmente ela tem 3 itens: uma espada, uma poção e um escudo. Ao longo da aventura encontra um arco no chão
#E precisar decidir se o coloca na mochila ou não. Caso coloque, precisará descartar outro item a sua escolha. Faça um programa simulando essa história e decisão usando lista/vetor

itens = ["espada", "poção", "escudo"]
print(f"Seus itens são: {itens}")
arco_adicional = input("Digite arco para colocar na mochila\n")

if arco_adicional == "arco":
    print("Arco adicionado!")
    itens.append(arco_adicional)
    remover_item = input("Qual item deseja remover?\n").lower()
    itens.remove(remover_item)
    print(f"A sua lista atual com o arco encontrado",itens)
else:
    print("Continue a sua jornada sem o arco!")