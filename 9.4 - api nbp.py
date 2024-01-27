import requests
from pydantic import BaseModel
from typing import List

# http://api.nbp.pl/api/exchangerates/rates/{table}/{code}/
url = 'http://api.nbp.pl/api/exchangerates/rates/A/USD/'

page = requests.get(url)
json = page.json()
print(json)
rates_usd = json['rates'][0]['mid']
print(rates_usd)


url2 = 'http://api.nbp.pl/api/exchangerates/rates/A/EUR/'

page1 = requests.get(url2)
json1 = page1.json()
print(json1)
rates_eur = json1['rates'][0]['mid']
print(rates_eur)


class Rate(BaseModel):
    mid:float

class Nbp (BaseModel):
    rates:List[Rate]

