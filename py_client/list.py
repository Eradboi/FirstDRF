import requests

endpoint = 'http://localhost:5000/api/products/'
get_response = requests.get(endpoint)
print(get_response.json())
# Rest API's mostly return json
# the can be consumed by a lot of clients at once