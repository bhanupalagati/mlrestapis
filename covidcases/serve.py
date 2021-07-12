# This files purpose is to serve the covid cases information as a restAPI
from flask_restful import Resource
from flask import jsonify
import pickle

file_name = "covidcases/covidreport.pkl"
open_file = open(file_name, "rb")
# [activecases, newcases, training, testing, future]
loaded_list = pickle.load(open_file)
open_file.close()

class CovidCases(Resource):
    def get(self):
        resp = {"result": loaded_list}
        return jsonify(resp)
