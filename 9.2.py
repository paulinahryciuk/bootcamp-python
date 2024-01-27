import requests
from pydantic import BaseModel

url = 'https://randomuser.me/api/'
response = requests.get(url)
print(response)
print(response.text)
data = response.json()

# class Resultss(BaseModel)

results = data['results']
print("-----")
print(results)
name = results[0]
print(name)
name1 = name['name']
print(name1)
name2 = name['name']['first']
print(name2)
photo_url = name['picture']['large']
print(photo_url)

response_photo = requests.get(photo_url)
with open('user_photo.jpg','wb') as f:
    f.write(response_photo.content)
