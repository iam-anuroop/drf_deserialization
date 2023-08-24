import json
import requests

URL = 'http://127.0.0.1:8000/stucre/'

data = {
    'name':'anuroop',
    'roll':33,
    'city':'blsry'
}
json_data = json.dumps(data)
print(json_data)
r = requests.post(url=URL,data=json_data)
print(r)
data = r.json()
print(data)

