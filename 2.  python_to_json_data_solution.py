import json


class User:
    def __int__(self, name, age, address, languages):
        self.name = name
        self.age = age
        self.address = address
        self.languages = languages


if __name__ == "__main__":
    user_01 = User()
    user_01.name = "Joao"
    user_01.age = 20
    user_01.address = "Av. Black Panther"
    user_01.languages = ["English", "French"]

    json_object = json.dumps(user_01.__dict__)

# To write JSON to a file in Python, we can use json.dump() method.

    with open('user.txt', 'w') as json_file:
        json.dump(json_object, json_file)
