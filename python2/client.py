import requests

r = requests.get('http://localhost:9020/cgi-bin/webapi_v1.py')

print(r.status_code)
print(r.json())
