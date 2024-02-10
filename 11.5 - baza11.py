from sqlalchemy import (
Column, Integer, String, ForeignKey, create_engine
)

from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()

class Parent(Base):
    __tablename__ = 'parents'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    children = relationship("Child", backref = 'parent')

class Child(Base):
    __tablename__ = 'children'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    parent_id = Column(Integer, ForeignKey('parents.id'))

engine = create_engine('sqlite:///:memory:', echo=True)

Base.metadata.create_all(engine)

Session = sessionmaker(bind = engine)
session = Session()

parent = Parent(name = "Rodzic")
child1 = Child(name = "dziecko1", parent= parent)
child2 = Child(name = "dziecko2", parent= parent)

session.add(parent)
session.add(child1)
session.add(child2)
session.commit()

our_parent = session.query(Parent).all()
print(our_parent)
our_parent_filtered = session.query(Parent).filter_by(name = "Rodzic").first()
print(f"rodzic {our_parent_filtered.name}")
for child in our_parent_filtered.children:
    print(f"dziecko {child.name}")