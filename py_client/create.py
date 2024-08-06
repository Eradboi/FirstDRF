import requests

endpoint = 'http://127.0.0.1:5000/api/products/'
data = {
    'title':'Knor Chicken'}
get_response = requests.post(endpoint,json=data)
print(get_response.json())