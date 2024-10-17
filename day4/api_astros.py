# Działanie   	  Instrukcja SQL	    HTTP	             DDS
# Create	          INSERT	       PUT / POST	        write
# Read (Retrieve)	  SELECT	       GET	                read / take
# Update              UPDATE	       POST / PUT / PATCH	write
# Delete (Destroy)    DELETE	       DELETE	            dispose
from pprint import pprint
from typing import List

from pydantic import BaseModel
import requests

# pip install requests
url = "http://api.open-notify.org/astros.json"

response = requests.get(url)
print(response)  # <Response [200]>
# https://pl.wikipedia.org/wiki/Kod_odpowiedzi_HTTP
print(response.text)
response_data = response.json()  # zamian jsona na slownik
print(type(response_data))  # <class 'dict'>

print(response_data.keys())
for i in response_data:
    print(i)
# dict_keys(['people', 'number', 'message'])
# people
# number
# message
pprint(response_data['people'])


# [{'craft': 'ISS', 'name': 'Oleg Kononenko'},
#  {'craft': 'ISS', 'name': 'Nikolai Chub'},
#  {'craft': 'ISS', 'name': 'Tracy Caldwell Dyson'},
#  {'craft': 'ISS', 'name': 'Matthew Dominick'},
#  {'craft': 'ISS', 'name': 'Michael Barratt'},
#  {'craft': 'ISS', 'name': 'Jeanette Epps'},
#  {'craft': 'ISS', 'name': 'Alexander Grebenkin'},
#  {'craft': 'ISS', 'name': 'Butch Wilmore'},
#  {'craft': 'ISS', 'name': 'Sunita Williams'},
#  {'craft': 'Tiangong', 'name': 'Li Guangsu'},
#  {'craft': 'Tiangong', 'name': 'Li Cong'},
#  {'craft': 'Tiangong', 'name': 'Ye Guangfu'}]

# {'craft': 'ISS', 'name': 'Michael Barratt'}
class Astronaut(BaseModel):
    name: str
    craft: str


class AstrosData(BaseModel):
    message: str
    people: List[Astronaut]
    number: int


data = AstrosData(**response.json())
pprint(data)
# AstrosData
# (message='success',
# people=[Astronaut(name='Oleg Kononenko', craft='ISS'),
# Astronaut(name='Nikolai Chub', craft='ISS'),
# Astronaut(name='Tracy Caldwell Dyson', craft='ISS'),
# Astronaut(name='Matthew Dominick', craft='ISS'),
# Astronaut(name='Michael Barratt', craft='ISS'),
# Astronaut(name='Jeanette Epps', craft='ISS'),
# Astronaut(name='Alexander Grebenkin', craft='ISS'),
# Astronaut(name='Butch Wilmore', craft='ISS'),
# Astronaut(name='Sunita Williams', craft='ISS'),
# Astronaut(name='Li Guangsu', craft='Tiangong'),
# Astronaut(name='Li Cong', craft='Tiangong'),
# Astronaut(name='Ye Guangfu', craft='Tiangong')],
# number=12)

for astronaut in data.people:
    print(f"{astronaut.name}, {astronaut.craft}")
# Oleg Kononenko, ISS
# Nikolai Chub, ISS
# Tracy Caldwell Dyson, ISS
# Matthew Dominick, ISS
# Michael Barratt, ISS
# Jeanette Epps, ISS
# Alexander Grebenkin, ISS
# Butch Wilmore, ISS
# Sunita Williams, ISS
# Li Guangsu, Tiangong
# Li Cong, Tiangong
# Ye Guangfu, Tiangong
