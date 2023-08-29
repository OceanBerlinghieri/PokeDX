import requests
"""Show info about specified berry"""

def show(berry):
    url = "https://pokeapi.co/api/v2/berry/" + berry.lower()
    
    response = requests.get(url)
    if response.status_code == 200:
        response_json = response.json()
        print("Berry:", berry)
        print("Id:", response_json['id'])
        print("Growth time:", response_json['growth_time'], "days")
        print("Max to own:", response_json['max_harvest'])
        print("Size:", response_json['size'])
    else:
        print("Error", response.status_code)
        
            
    option = input("Do you want to continue? (Y/N): ").lower()
    
    if option == 'y':
        berry = input("What berry do you want to know about?: ")
        show(berry)


if __name__ == '__main__':
    berry = input("What berry do you want to know about?: ")
    show(berry)

    
