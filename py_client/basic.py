import requests

endpoint = 'http://localhost:5000/api/'
get_response = requests.post(endpoint, params={'abc':123},json={'title':"Nestle Milo",'about':'Hello Earth','price':120})
print(get_response.json())
# Rest API's mostly return json
# the can be consumed by a lot of clients at once