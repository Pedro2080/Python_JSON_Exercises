import json


def dictionary():

    key_value = {"2":20, "1": 2, "5": 12, "4": 20, "6": 10}

    print(f"Original key_value {key_value}")

    sorted_obj = dict(sorted(key_value.items(), key=lambda keyval: (keyval[0], keyval[1])))

    print(f"Sorted by key value: {json.dumps(sorted_obj, indent=4)}")


def main():
    dictionary()


if __name__ == "__main__":
    main()
