from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods =["GET", "POST"])
def home():
    
    #Si se solicita la página web, simplemente la devolvemos
    #Añadir devolución de lista de pokemons
    if request.method == "GET":
        return render_template('index.html')
    
    #Si en el formulario creado en nuestra web se produce un post, añadimos a la URL la busqueda y solicitamos los datos Json
    if request.form['search']:
        url = "https://pokeapi.co/api/v2/pokemon/" + request.form['search']
        response = requests.get(url)
        response_json = response.json()
        return render_template('index.html', data=response_json)
    
    #Si el campo de búsqueda está vacío, devolvemos el template básico
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)