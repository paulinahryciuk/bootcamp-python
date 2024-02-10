from sqlalchemy import (
Column, Integer, String, ForeignKey, create_engine
)

from sqlalchemy.orm import relationship, sessionmaker, declarative_base

# engine = create_engine('sqlite:///:memory:')
engine = create_engine('sqlite:///adress_book.db', echo= True)
Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(String)
    addresses = relationship(
        'Address',
        back_populates = 'person',
        order_by = 'Address.email',
        cascade='all, delete-orphan',
        )


    def __repr__(self):
        return f"{self.name} (id = {self.id})"
class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    person_id = Column(ForeignKey('person.id'))
    person = relationship("Person", back_populates='addresses')

    def __str__(self):
        return self.email

    __repr = __str__

Base.metadata.create_all(engine)
Session = sessionmaker(bind= engine)

session = Session()

anakin = Person(name = "an", age = '38')
anakin2 = Person(name = "an an", age = '38')
anakin2.address = [Address(email = 'anan@')]
obi = Person(name = "obi", age = 45)
obi.address = [
    Address(email = "@@"),
    Address(email = "@@aa")
]

session.add(anakin)
session.add(anakin2)
session.add(obi)
session.commit()

all_ = session.query(Person).all()
print(all_)

an1 = session.query(Person).first()
print(an1)
print(type(an1))
print(an1.name, an1.age)

obi_list = session.query(Person).filter(
    Person.name.like('Obi%')
).all()
print("----------")
for o in obi_list:
    print('id=', o.id, 'name', o.name, "wiek", o.age, "email" , o.addresses)
