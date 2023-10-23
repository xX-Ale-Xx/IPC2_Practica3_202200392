import json
from flask import Flask, request

app = Flask(__name__)
movies = []
@app.route("/")
def index():
    return "Bienvenido"

@app.route("/api/new-movie", methods=["POST"])
def add_movie():
    movie_data = request.get_json()
    movies.append(movie_data)
    return "message: La película fue agregada con éxito"

@app.route("/api/all-movies-by-genre/<genre>", methods=["GET"])
def get_movies_by_genre(genre):
    filtered_movies = [movie for movie in movies if movie["genre"] == genre]

    # Devolver una respuesta
    return json.dumps(filtered_movies)

@app.route("/api/update-movie", methods=["PUT"])
def update_movie():
    movie_data = request.get_json()
    for movie in movies:
        if movie["movieId"] == movie_data["movieId"]:
            movie["name"] = movie_data["name"]
            movie["genre"] = movie_data["genre"]
            break

    
    return "message: La película fue actualizada con éxito"

if __name__ == "__main__":
    app.run(debug=True)