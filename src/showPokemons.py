import requests
"""Shows a number of pokemons in the pokedex order
if user continues shows the next number of pokemons"""

def show(limit = 20, offset = 0):
    url = "https://pokeapi.co/api/v2/pokemon/"
    args = {'limit' : limit, 'offset' : offset}
    
    response = requests.get(url, params = args)
    if response.status_code == 200:
        response_json = response.json()
        for pokemon in response_json['results']:
            print(pokemon['name'].capitalize())
            
    option = input("Do you want to continue? (Y/N): ").lower()
    
    if option == 'y':
        offset += int(limit)
        show(limit, offset)


if __name__ == '__main__':
    limit = input("How many pokemons do you want in each list?: ")
    show(limit)
    
