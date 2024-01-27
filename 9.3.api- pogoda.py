import requests
from datetime import datetime
# https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
url = 'http://api.openweathermap.org/data/2.5/weather?q=Warszawa&appid=-KEY TUTAJ TOKEN'

page = requests.get(url)
json = page.json()
print(json)

desc = json['weather'][0]['description']
print(desc)
temp = json['main']['temp']
print(temp)
name = json['name']
print(name)
sunrise = json['sys'] ['sunrise']
print(sunrise)
dt_object = datetime.fromtimestamp(sunrise)
print(dt_object)