import pickle

lista = [1,2,3,4,5]
print(type(lista))

with open("lista.txt","w") as f:
    f.write(str(lista))

with open('lista.txt','r') as fh:
    lines = fh.read()

print(lines)
print(type(lines))


with open("lista.pickle","wb") as f :
    pickle.dump(lista, f)

with open("lista.pickle", 'rb') as fh:
    p = pickle.load(fh)

print(p)
print(type(p))
lista_ser = pickle.dumps(lista)
print(lista_ser)
print(pickle.loads(lista_ser))