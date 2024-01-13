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

