import pickle

slownik = {"imie": "Adam", "nazwisko":"Nowak", "wiek":50}

with open("slownik.pikle", "wb") as f:
    pickle.dump(slownik,f)

with open("slownik.pikle", "rb") as fh:
    p = pickle.load(fh)

print(p)
