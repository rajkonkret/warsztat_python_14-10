from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

engine = create_engine('sqlite:///moja_baza_danych.db')
Base = declarative_base()


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    books = relationship('Book', back_populates='author')


class Publisher(Base):
    __tablename__ = 'publishers'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))

    books = relationship('Book', back_populates='publisher')


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))
    publisher_id = Column(Integer, ForeignKey('publishers.id'))

    author = relationship("Author", back_populates='books')
    publisher = relationship("Publisher", back_populates='books')


Base.metadata.create_all(engine)
Sesssion = sessionmaker(bind=engine)
session = Sesssion()

new_author = Author(name="Adam Mickiewicz")
new_publisher = Publisher(name="Wydawnictwo XYZ")
new_book = Book(title="Pan Tadeusz", author=new_author, publisher=new_publisher)

session.add_all(
    [new_author, new_publisher, new_book]
)

session.commit()

authors = session.query(Author).all()
print(authors)

for author in authors:
    print(f"Author: {author.name}")
    for book in author.books:
        print(f"Książka {book.title}, wydawca {book.publisher.name}")
# Author: Adam Mickiewicz
# Książka Pan Tadeusz, wydawca Wydawnictwo XYZ
# Author: Adam Mickiewicz
# Książka Pan Tadeusz, wydawca Wydawnictwo XYZ
# Author: Adam Mickiewicz
# Książka Pan Tadeusz, wydawca Wydawnictwo XYZ
# Author: Adam Mickiewicz
# Książka Pan Tadeusz, wydawca Wydawnictwo XYZ
# Author: Adam Mickiewicz
# Książka Pan Tadeusz, wydawca Wydawnictwo XYZ

publishers = session.query(Publisher).all()
for publisher in publishers:
    print(f'Wydawca: {publisher.name}')
    for book in publisher.books:
        print(f"Ksiązka {book.title}")
        print(f"Author: {book.author.name}")
# Author: Adam Mickiewicz
# Książka Pan Tadeusz, wydawca Wydawnictwo XYZ
# Wydawca: Wydawnictwo XYZ
# Ksiązka Pan Tadeusz
# Author: Adam Mickiewicz
# Wydawca: Wydawnictwo XYZ
# Ksiązka Pan Tadeusz
# Author: Adam Mickiewicz
# Wydawca: Wydawnictwo XYZ
# Ksiązka Pan Tadeusz
# Author: Adam Mickiewicz
# Wydawca: Wydawnictwo XYZ
# Ksiązka Pan Tadeusz
# Author: Adam Mickiewicz
# Wydawca: Wydawnictwo XYZ
# Ksiązka Pan Tadeusz
# Author: Adam Mickiewicz
# Wydawca: Wydawnictwo XYZ
# Ksiązka Pan Tadeusz
# Author: Adam Mickiewicz
# Wydawca: Wydawnictwo XYZ
# Ksiązka Pan Tadeusz
# Author: Adam Mickiewicz
