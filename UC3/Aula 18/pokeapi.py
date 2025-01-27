import requests

def buscar_pokemon(nome_pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{nome_pokemon}"
    response = requests.get(url)
    dados_pokemon = response.json()

    if response.status_code == 200:
        print(f"Nome: {dados_pokemon['name']}")
        print(f"Tipo(s): {', '.join([tipo['type']['name'] for tipo in dados_pokemon['types']])}")
        print(f"Altura: {dados_pokemon['height']} dm")
        print(f"Peso: {dados_pokemon['weight']} hg")
    else:
        print("Pokémon não encontrado.")

buscar_pokemon("pikachu")