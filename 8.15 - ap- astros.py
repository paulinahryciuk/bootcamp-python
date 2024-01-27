import requests
from pydantic import BaseModel
from typing import (List)


url = 'http://api.open-notify.org/astros.json'
response = requests.get(url)
print(response)

response_data = response.json()
print(type(response_data))

for k,v in response_data.items():
    print((k, "=>", v))

for i in response_data['people']:
    print(i)

print(response_data['people'][2]['name'])

class Astronaut(BaseModel):
    name:strcraft:str

class AsroData