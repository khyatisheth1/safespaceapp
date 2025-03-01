import json
import tkinter as tk
from tkinter import messagebox

def get_user_info():
    user_info = {}
    user_info['name'] = name_entry.get()
    user_info['email'] = email_entry.get()
    user_info['age'] = age_entry.get()
    return user_info

def save_user_info(user_info, filename='user_info.json'):
    with open(filename, 'w') as file:
        json.dump(user_info, file, indent=4)
    messagebox.showinfo("Success", f"User information saved to {filename}")

def loa