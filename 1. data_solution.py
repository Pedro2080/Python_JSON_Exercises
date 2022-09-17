import json

class User:
    def __init__(self, guid, is_active, name, email, phone, address):

        self.guid = guid
        self.is_active = is_active
        self.first_name = name['first']
        self.last_name = name['last']
        self.email = email
        self.phone = phone
        self.address = address

    @classmethod
    def from_json(cls, json_string):
        json_dict = json.loads(json_string)  # json.loads() returns a Python dictionary

        return cls(**json_dict)

    def __repr__(self):
        return f'User: {self.first_name}'


json_string_ = '''{
    "guid": "1f1c4ac7-fc36-4008-935b-d87ffc7d8700",
    "is_active": false,
    "name": {
        "first": "Joao",
        "last": "Silva"
    },
    "email": "rjoaopedro2080@hotmail.com",
    "phone": "+ 48 758 785 412",
    "address": "AV. New York-USA"
}'''

print(type(json_string_))
user = User.from_json(json_string_)
print(user)
print(user.email)
print(user.phone)

# Let's use the json.loads() method to read a file containing JSON object

users_list = []
with open('1. data.json', 'r') as json_file:
    user_data = json.load(json_file)

    for x in user_data:
        users_list.append(User(**x))

print(users_list)
