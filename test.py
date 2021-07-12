import requests

BASEURL = 'http://127.0.0.1:5000/'

response = requests.get(BASEURL + "covidcases/activecases")
print(response.data)
