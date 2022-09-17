import json

file = "states.json"


def write_json(data, filename="new_file_data.json"):
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)


with open(file, 'r') as json_file:
  state_data = json.loads(json_file.read())

  write_json(state_data)

