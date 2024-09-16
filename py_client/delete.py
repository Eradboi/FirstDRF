import requests
product_id = input("What is the product id that you want to delete?")
endpoint = f'http://127.0.0.1:5000/api/products/{int(product_id)}/delete'
# since we are updating it
Headers = {
    'Authorization': "Bearer ad9e35489598061678dc8c6c4710e8a6fc919685"
}
get_response = requests.delete(url=endpoint, headers=Headers)
print(get_response.text)