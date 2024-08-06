import requests

endpoint = 'http://127.0.0.1:5000/api/products/2/update'

data = {
    'title':'Barber Chair'}
# since we are updating it
get_response = requests.put(endpoint,json=data)
print(get_response.json())