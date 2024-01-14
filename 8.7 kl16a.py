import pickle
from kl10 import Person

with open("dane.pikle",'rb') as file:
    p = pickle.load((file))

print(p)
print(type(list))

for person in p:
    print(person)

for person in p:
    person.greets()