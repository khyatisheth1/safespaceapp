import tkinter as tk
from tkinter import messagebox
from user_storage import store_user_info

class SignUpScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Sign Up")

        self.username_label = tk.Label(root, text="Username")
        self.username_label.pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        self.password_label = tk.Label(root, text="Password")
        self.password_label.pack()
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()

        self.signup_button = tk.Button(root, text="Sign Up", command=self.signup)
        self.signup_button.pack()

    def signup(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username and password:
            store_user_info(username, password)
            messagebox.showinfo("Success", "User signed up successfully!")
        else:
            messagebox.showwarning("Error", "Please enter both username and password.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SignUpScreen(root)
    root.mainloop()
