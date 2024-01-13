class Defoultdict(dict):
    def __missing__(self, key):
        self ['key'] = "randomowy"
        return "klucz_domyslny"
        return key

d_python = {}
d2 = Defoultdict()
print(d2["kluczyk"])
print(d2.keys())
print(d2[kl])

class Slownik(dict):
    def __missing__(self, key):
        if isinnstance(key, str)
        return self[key.lower()]

d3 = Slownik()
d3["name"] = ("Radek")
print(d3["Name"])