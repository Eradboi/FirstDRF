import requests
headers = {
        'Authorization': "Bearer e61aa4e523c4ecfcf8d8822dd7cb32cb05f6f523"
    }
endpoint = 'http://127.0.0.1:5000/api/products/'
data = {
    'title':'Knor Chicken'}
get_response = requests.post(endpoint,json=data, headers=headers)
print(get_response.json())