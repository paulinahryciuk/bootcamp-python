import pickle
from dataclasses import dataclass

# class Person:
#     def __init__(self,fn, ln, id):
#         self.fn = fn
#         self.ln = ln
#         self.id = id
#
# p1 = Person("Jan","Kowalski",1)

@dataclass
class Person:
    first_name: str
    last_name: str
    id: str

    def greets(self):
        print(f"witam jestem {self.first_name} {self.last_name}, Td to {self.id}")

p1 = Person("Jan","Kowalski",1)
print(p1)
p2 = Person("Maciej","Nowak",2)
print(p1)

people = [p1,p2]

with open("dane.pikle",'wb') as stream:
    pickle.dump(people,stream)

