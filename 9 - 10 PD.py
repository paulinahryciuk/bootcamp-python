import requests
from pydantic import BaseModel

# url = 'http://numbersapi.com/#42'
# url = 'http://numbersapi.com/3'
# response =requests.get(url)
# print(response)
# print(response.text)
# print("----------------")
# url2 = 'http://numbersapi.com/3/math'
# response2 =requests.get(url2)
# print(response2)
# print(response2.text)
#
# url3 = 'http://numbersapi.com/100/?json'
# response3 =requests.get(url3)
# print(response3)
# print(response3.text)

url4 = 'https://api.chucknorris.io/jokes/random'
url4 = 'https://api.chucknorris.io/jokes'
response4 =requests.get(url4)
print(response4)
print(response4.text)
response = requests.get(url)
print(response.text)
print(response)

ur  = 'https://restcountries.com/v3.1/name/Greece'
response = requests.get(ur)
print(response)
print(response.text)
slownik = response.json()
slownik2 = slownik[0]
print(slownik2['name'])
print(slownik2['name']['official'])
# print(slownik2['translation'])

class Name(BaseModel):
    common: str
    official: str
class Pierwsza(BaseModel):
    name : Name

ob1 = Pierwsza()
print(ob1.Name)
data = [Pierwsza(**kwargs) for k in slownik]
for d in data:
    print(i)
print(Pierwsza.name.official)