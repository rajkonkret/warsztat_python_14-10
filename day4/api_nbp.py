from bdb import effective
from locale import currency
from pprint import pprint
from typing import List

from pydantic import BaseModel
import requests

from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, Float
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

engine = create_engine('sqlite:///currencies_db.db')
Base = declarative_base()

url = "https://api.nbp.pl/api/exchangerates/rates/A/USD/"
response = requests.get(url)
print(response)  # <Response [200]>
# https://pl.wikipedia.org/wiki/Kod_odpowiedzi_HTTP
print(response.text)
response_data = response.json()  # zamian jsona na slownik
print(type(response_data))


# {"table": "A", "currency": "dolar amerykański", "code": "USD",
#  "rates": [{"no": "203/A/NBP/2024", "effectiveDate": "2024-10-17", "mid": 3.9786}]}

class Rates(BaseModel):
    no: str
    effectiveDate: str
    # mid: int  #  Input should be a valid integer, got a number with a fractional part [type=int_from_float, input_value=3.9786, input_type=float]
    mid: float


class Currency(BaseModel):
    table: str
    currency: str
    code: str
    rates: List[Rates]


data = Currency(**response.json())
pprint(data)
print(data.rates[0].mid)  # 3.9786


# Currency(table='A', rates=[Rates(no='203/A/NBP/2024', effectiveDate='2024-10-17', mid=3.9786)])

class RatesDB(Base):
    __tablename__ = 'rates'
    id = Column(Integer, primary_key=True)
    no = Column(String)
    effectiveDate = Column(String)
    mid = Column(Float)
    currency_id = Column(ForeignKey('currency.id'))
    currencies = relationship("CurrencyDB", back_populates='rates')


class CurrencyDB(Base):
    __tablename__ = 'currency'
    id = Column(Integer, primary_key=True)
    table = Column(String)
    currency = Column(String)
    code = Column(String)
    rates = relationship("RatesDB", back_populates='currencies', cascade='all')


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

session = Session()
rates_list = []

for i in data.rates:
    rates_list.append(
        RatesDB(
            no=i.no,
            effectiveDate=i.effectiveDate,
            mid=i.mid))
usd = CurrencyDB(
    table=data.table,
    currency=data.currency,
    code=data.code,
    rates=rates_list)
usd.rates = rates_list

# usd = CurrencyDB(table=data.table)
session.add(usd)
session.commit()
