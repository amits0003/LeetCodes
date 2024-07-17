from datetime import datetime
from typing import Tuple

from pydantic import BaseModel


class Address(BaseModel):
    street: str
    city: str
    country: str


class User(BaseModel):
    id: int
    name: str
    age: int
    email: str
    address: Address


user_data = {
    'id': 123,
    'name': 'John Doe',
    'age': 30,
    'email': 'john.doe@example.com',
    'address': {
        'street': '123 Main St',
        'city': 'Anytown',
        'country': 'USA'
    }
}
try:
    user = User(**user_data)
    print(user)
except Exception as e:
    print("error" , e)


# use case 3 :

import json

json_data = '''
{
    "id": 123,
    "name": "John Doe",
    "age": 30,
    "email": "john.doe@example.com",
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "country": "USA"
    }
}
'''

user_data = json.loads(json_data)
user = User(**user_data)
print(user)