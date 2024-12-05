# Criando uma lista simples com 3 Pokémons
pokemons = ["Pikachu", "Charmander", "Bulbasaur"]

# Exibindo a lista
print("Lista de Pokémons:", pokemons)

# Acessando o primeiro Pokémon da lista
print("Primeiro Pokémon:", pokemons[0])

#Adicionando um novo Pokémon à lista
pokemons.append("Squirtle")
print("Lista de Pokémons após adicionar Squirtle:", pokemons)

# Removendo o Pokémon "Charmander" da lista
pokemons.remove("Charmander")
print("Lista de Pokémons após remover Charmander:", pokemons)

#Exibindo o tamanho da lista
print("Numero de Pokémons na lista:", len(pokemons))