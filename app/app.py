from flask import Flask, render_template
from services import PokemonService

app = Flask(__name__, template_folder="templates")
pokemon_service = PokemonService()


@app.route("/")
def hello_geek():
    pokemon = pokemon_service.get_random_pokemon()
    return render_template("index.html", pokemon=pokemon)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
