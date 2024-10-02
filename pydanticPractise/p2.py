from pydantic import BaseModel, ValidationError


class User(BaseModel):
    id: int
    name: str
    age: int
    email: str


# Example data
user_data = {
    'id': 123,
    'name': 'John Doe',
    'age': 30,
    'email': 'john.doe@example.com'
}

# Creating an instance of User
user = User(**user_data)
print(user)
print(user.id, user.name, user.age, user.email)

invalid_user_data = {
    'id': 'not_an_int',
    'name': 'John Doe',
    'age': 30,
    'email': 'john.doe@example.com'
}

try:
    invalid_user = User(**invalid_user_data)
except ValidationError as e:
    print(e)
