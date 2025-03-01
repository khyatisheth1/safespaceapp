import json
import os

USER_DATA_FILE = "user_data.json"

def store_user_info(username, password):
    user_data = {
        "username": username,
        "password": password
    }
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "r") as file:
            data = json.load(file)
    else:
        data = []

    data.append(user_data)

    with open(USER_DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)
