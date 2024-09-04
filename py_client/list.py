import requests
from getpass import getpass
password = getpass()
endpoint = 'http://localhost:5000/api/auth/'
token = requests.post(endpoint, json={'username':'Erad', 'password':password})
print(token.json())

if token.status_code == 200:
    tok = token.json()['token']
    headers = {
        'Authorization': f"Bearer {tok}"
    }
endpoint = 'http://localhost:5000/api/products/'
get_response = requests.get(endpoint, headers=headers)
print(get_response.json())
# Rest API's mostly return json
# the can be consumed by a lot of clients at once