dictionary = {'imie':"Radek", "nazwisko":"Kowalski"}
print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())

for k,v in dictionary.items():
    print((k, "=>", v))
