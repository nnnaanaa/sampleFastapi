import requests

# res = requests.get('http://localhost:8092/sample')
# res = requests.get('http://localhost:8092/items/?skip=1&limit=2')

# res = requests.post('http://localhost:8092/items/',
#                     json={"name": "Tシャツ", "price": 2000, "description": "白Tシャツ"},
# )   

res = requests.get('http://localhost:8092/sample',
                   headers={"Authorization": "Bearer A1B2C3D4"})             

print(res.status_code)
print(res.text)