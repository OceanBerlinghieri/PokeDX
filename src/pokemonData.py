import requests
"""Shows basic data of a specified pokemon, such as
name, pokedex id, tpyes and the number of games it has appearence"""
def show(pokemon):
    url = "https://pokeapi.co/api/v2/pokemon/" + pokemon
    
    response = requests.get(url)
    if response.status_code == 200:
        response_json = response.json()
        print("Pokemon:", pokemon.capitalize())
        print("Pokemon ID:", response_json['id'])
        types = response_json['types']
        print("Types:")
        for type in types:
            print(" -", type['type']['name'].capitalize())
        print("Appears in:", len(response_json['game_indices']), "games")
    else: 
        print("Error", response.status_code)
        
            
    option = input("Do you want to know about another pokemon? (Y/N): ").lower()
    
    if option == 'y':
        pokemon = input("Introduce a pokemon: ").lower()
        show(pokemon)


if __name__ == '__main__':
    pokemon = input("Introduce a pokemon: ").lower()
    show(pokemon)
    
