
usuario = input("gostaria de substituir algum poder no pikachu? S/N\n ").lower()
qual = input("qual gostaria de adciona? ").lower()
poder = input("qual poder gostaria de retirar? ")

pikachu = ["choque do trovão", "calda de ferro", "ataque rapido", "esquiva"]
print("lista de de poder", pikachu)
print("Primeiro poder", pikachu[0])
pikachu.append(f"{qual}")
print(f"Lista de poder após adicionar {qual}", pikachu)
pikachu.remove(f"{poder}")
print(f"lista de poder após remover o {poder}", pikachu)
print("esse são as quantidades de poderes do pikachu", len(pikachu))