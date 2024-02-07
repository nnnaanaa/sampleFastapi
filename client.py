import requests

r = requests.get('http://web_server:5000?argument1=ui&argument2=be&argument3=am')
print(r.status_code)
print(r.json())
