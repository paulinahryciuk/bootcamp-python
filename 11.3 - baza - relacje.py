from sqlalchemy import (
Column, Integer, String, ForeignKey, create_engine
)

from sqlalchemy, orm import relationship, sessionmaker, declarative_base

# engine = create_engine('sqlite:///:memory:')
engine = create_engine('sqlite:///adress_book.db', echo= True)
Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(String)
    address = relationship(
        'Address',
        back_populatess = 'person',
        order_by = 'Adress.email',
        cascade='all, delete-orphan',
        )


    def __repr__(self):
        return f"{self.name} (id = {self.id})"
class Adress(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    person_id = Column(ForeignKey('person.id'))

    def __str__(self):
        return self.email

    __repr = __str__

Base.metadata
