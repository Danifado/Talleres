import requests
from Talleres.Decoradores.decorators import consulta_tipo


class Proxy:
    def __init__(self, instance):
        self.instance = instance

    def proxy(self):
        object_instance = self.instance
        pokemon_name = object_instance.pokemon
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
        if (response).status_code == 200:
            json_data = response.json()
            json_data = json_data["types"]
            if (len(json_data) > 1):
                return "You can not query more than 2 types at once"
            else:
                pass
            json_data = json_data[0]["type"]
            pokemon_type = json_data['name']
            response_2 = requests.get(f"https://pokeapi.co/api/v2/type/{pokemon_type}")
            if response_2.status_code == 200:
                json_data_2 = response_2.json()["damage_relations"]
                double_damage_type = json_data_2["double_damage_from"][0]["name"]
        return f"The pokemon type that deals doble damage against {pokemon_name} is: {double_damage_type}"