import json

def save_data(data):

    with open("participants.json", "w") as file:
        json.dump(data, file, indent=4)

def open_data():

    try:
        with open("participants.json", "r") as file:
            data = json.load(file)
            return data

    except FileNotFoundError:
        return[]

    except json.JSONDecodeError:
        return []
