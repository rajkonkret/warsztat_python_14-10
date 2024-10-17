# sqlalchemy - system orm do pracy z bazą danych w sposób obiektowy
# pip install sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

engine = create_engine('sqlite:///:memory:')
Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(String)
    addresses = relationship("Address",
                             back_populates="person",
                             order_by='Address.email',
                             cascade='all, delete-orphan')

    def __repr__(self):
        return f"{self.name} (id={self.id})"


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    person_id = Column(ForeignKey('person.id'))
    person = relationship("Person", back_populates='addresses')

    def __str__(self):
        return self.email

    __repr__ = __str__


# encje - kalsy odwzorowujące tabele w bazie danych

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

session = Session()
anakin = Person(name='Anakin', age=38)
obi = Person(name="OBI WAN Kenobi", age=45)
obi.addresses = [
    Address(email='obi@example.com'),
    Address(email='waaka@example.com'),
]
obi2 = Person(name='obi', age=54)

session.add(anakin)
session.add(obi)
session.add(obi2)
session.commit()

all_ = session.query(Person).all()
print(all_)  # [Anakin (id=1), OBI WAN Kenobi (id=2), obi (id=3)]

an1 = session.query(Person).first()
print(an1)
print(type(an1))
print(an1.id, an1.name, an1.addresses)
# Anakin (id=1)
# <class '__main__.Person'>
# 1 Anakin []

obi_list = session.query(Person).filter(
    Person.name.like('Obi%')
).all()

print(obi_list)
for o in obi_list:
    print("id=", o.id, "name=", o.name, "age=", o.age, "email=", o.addresses)
# [OBI WAN Kenobi (id=2), obi (id=3)]
# id= 2 name= OBI WAN Kenobi age= 45 email= [obi@example.com, waaka@example.com]
# id= 3 name= obi age= 54 email= []
