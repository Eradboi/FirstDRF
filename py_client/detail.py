import requests

endpoint = 'http://127.0.0.1:5000/api/products/10/'
get_response = requests.get(endpoint)
print(get_response.json())