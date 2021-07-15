from flask import Flask, jsonify
from flask_restful import Api, Resource
from covidcases.serve import CovidCases
from pokemoncluster.serve import PokemonClusteredData, PokemonBorders, PokemonClassify

app = Flask(__name__)
api = Api(app)

class MainRoute(Resource):
    def get(self):
        return []

api.add_resource(MainRoute, "/")
api.add_resource(CovidCases, "/covidcases")
api.add_resource(PokemonClusteredData, "/pokemoncluster/data")
api.add_resource(PokemonBorders, "/pokemoncluster/borders")
api.add_resource(PokemonClassify, "/pokemoncluster/predict")

if __name__ == "__main__":
    app.run(debug=True)
