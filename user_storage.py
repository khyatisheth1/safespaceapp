import json
import os

USER_DATA_FILE = "user_data.json"

def store_user_info(username, password):
    user_data = {}
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "r") as file:
            user_data = json.load(file)
    
    user_data[username] = password
    
    with open(USER_DATA_FILE, "w") as file:
        json.dump(user_data, file)
