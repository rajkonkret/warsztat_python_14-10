from pprint import pprint
from typing import List

from pydantic import BaseModel
import requests

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
    # currency: str
    # code: str
    rates: List[Rates]


data = Currency(**response.json())
pprint(data)
print(data.rates[0].mid)  # 3.9786
# Currency(table='A', rates=[Rates(no='203/A/NBP/2024', effectiveDate='2024-10-17', mid=3.9786)])
