import requests
from pydantic import BaseModel

url = 'https://randomuser.me/api/'
response = requests.get(url)
print(response)
print(response.text)
data = response.json()

# class Results(BaseModel)

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

class Name(BaseModel):
     title:str
     first:str
     last:str



class User(BaseModel):
    name: Name
    email:str
    picture: dict

u1 = data['results'][0]
user = User(**u1)
print(user)

print(user.name.first)