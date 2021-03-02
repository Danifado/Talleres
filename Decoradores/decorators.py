import requests


def consulta_tipo(function):
    def wrapper(pokemon_type):
        pokemon_type = pokemon_type.lower()
        response = requests.get(f"https://pokeapi.co/api/v2/type/{pokemon_type}")
        if response.status_code == 200:
            json_data = response.json()
            pokemon_list = json_data["pokemon"]
            print(f"Estos son tipo {pokemon_type}: ")
            strong_pokemons = []
            for i in pokemon_list:
                strong_pokemons.append(i["pokemon"]["name"])
            return strong_pokemons
        else:
            return function()
    return wrapper
