import requests
# https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
url = 'http://api.openweathermap.org/data/2.5/weather?q=Warszawa&appid=99a24a78addf4a2c41947189fcff67f7&&lang=p&format=jsonl&units=metric'

page = requests.get(url)
json = page.json()
print(json)

desc = json['weather'][0]['description']
print(desc)
temp = json['main']['temp']
print(temp)
name = json['name']
print(name)