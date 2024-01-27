import requests as re

url = 'http://api.nbp.pl/api/exchangerates/tables/A/?format=xml'
response = re.get(url)
print(response)
print(response.text)

xml_data = response.content
print(xml_data)