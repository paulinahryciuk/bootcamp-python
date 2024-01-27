import requests

# url = 'https://restcountries.com/v3.1/name/{name}?fullText=true'
url = 'https://restcountries.com/v3.1/name/Poland'

response = requests.get(url)
print(response)
print(response.text)
response_data = response.json()
print(response_data[0])
data = response_data[0]
country = data[0]
print(f"nazwa kraju: {country['name']}")

class Pol(BaseModel):
    official: str
    common: str