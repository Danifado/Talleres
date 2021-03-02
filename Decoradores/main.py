# Daniel Andres Zarate Velez
# MACC 2021
# With this code you can give a pokemon type and you will get each pokemon that matches.


from Talleres.Decoradores.decorators import consulta_tipo


@consulta_tipo
def alerta_tipo(pokemon_tipo=None):
    return "It seems that this type is missing :("


pokemon_type = input("Input the pokemon type to look up: ")
print(alerta_tipo(pokemon_type))
