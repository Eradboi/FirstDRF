import requests
product_id = input("What is the product id that you want to delete?")
endpoint = f'http://127.0.0.1:5000/api/products/{int(product_id)}/delete'
# since we are updating it
get_response = requests.delete(endpoint)
print(get_response.status_code)