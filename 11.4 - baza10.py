from sqlalchemy import (
Column, Integer, String, ForeignKey, create_engine
)

from sqlalchemy.orm import relationship, sessionmaker, declarative_base

engine = create_engine("sqlite:///moja_baza_danych.db")
Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    books = relationship("Book", back_populates='author')
    # def __repr__(self):
    #     return f"{self.name}"

class Publisher(Base):
    __tablename__ = 'publishers'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    books = relationship("Book", back_populates='publisher')

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)

    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship('Author', back_populates='books')

    publisher_id = Column(Integer, ForeignKey('publishers.id'))
    publisher = relationship("Publisher", back_populates = 'books')

Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)
session = Session()

new_author = Author(name = 'Adam')
new_publisher = Publisher(name = "Wyd XYZ")
new_book = Book(title = "Pan Tadeusz", author = new_author, publisher  = new_publisher )

session.add_all(
    [new_author, new_publisher, new_book]
)
session.commit()

# autor= session.query(Author).all()
# print(autor)
# for autor in authors:
#     print(f'autor.{autor.name}')
#     print(f"Ksiazka {b.title}, wydawca: {b.publisher.name}")

wydawcy  = session.query(Publisher).all()
for wydawca in wydawcy:
    print(f"wydawca: {wydawca.name}")
    for book in wydawca.books:
        print(f"ksaizka {book.title}")

