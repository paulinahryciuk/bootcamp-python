import json

person_dict = {'name':'Radek', 'age':40, 'czy_pali': None}

with open('nasze_dane.json', 'w') as f:
    json.dump(person_dict,f, indent=4, sort_keys=True)

with open('nasze_dane.json','r') as file:
    data = json.load(file)

print((data))