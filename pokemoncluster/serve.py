# This files purpose is to serve the poekmon Clustering information as a restAPI
from flask_restful import Resource
from flask import jsonify, request
import pickle

file_name = "pokemoncluster/pokemonCluster.pkl"
open_file = open(file_name, "rb")
# [clusteredData, model, maxDetails, minDetails]
loaded_list = pickle.load(open_file)
open_file.close()

class PokemonClusteredData(Resource):
    def get(self):
        resp = loaded_list['clusterData']
        return jsonify(resp)

class PokemonBorders(Resource):
    def get(self):
        resp = {'maxDetails': loaded_list['maxDetails'], 'minDetails': loaded_list['minDetails']}
        return jsonify(resp)

class PokemonClassify(Resource):
    def post(self):
        model = loaded_list['model']
        value = request.json['data']
        prediction = model.predict([value])
        return int(prediction[0])
