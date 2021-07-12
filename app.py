from flask import Flask, jsonify
from flask_restful import Api, Resource
from covidcases.serve import CovidCases

app = Flask(__name__)
api = Api(app)


api.add_resource(CovidCases, "/covidcases")

if __name__ == "__main__":
    app.run(debug=True)
