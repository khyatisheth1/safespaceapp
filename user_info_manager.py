import json
import os
import tkinter as tk
from tkinter import messagebox

PT_DATA_FILE = "pt_data.json"

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

def save_emails(emails):
    pt_data = {}
    if os.path.exists(PT_DATA_FILE):
        with open(PT_DATA_FILE, "r") as file:
            pt_data = json.load(file)
    
    parent_email = emails.get('parentemail')
    teacher_email = emails.get('teacheremail')
    
    if parent_email:
        pt_data[parent_email] = {
            'type': 'parent'
        }
    
    if teacher_email:
        pt_data[teacher_email] = {
            'type': 'teacher'
        }
    
    with open(PT_DATA_FILE, "w") as file:
        json.dump(pt_data, file, indent=4)

