import requests

r = requests.get('http://web_server:5000/users/100/items/100?q=100&short=True')
print(r.status_code)
print(r.json())