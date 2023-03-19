import json


def read_json(file_path):
    # Open the JSON file
    with open(file_path, "r") as f:
        # Load the JSON data
        data = json.load(f)

    return data
