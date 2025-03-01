class SignupScreen:
    def __init__(self):
        self.username = ""
        self.email = ""
        self.password = ""

    def display_signup_form(self):
        print("Welcome to the Signup Screen")
        self.username = input("Enter your username: ")
        self.email = input("Enter your email: ")
        self.password = input("Enter your password: ")

    def collect_user_input(self):
        self.display_signup_form()

    def store_user_information(self):
        # Here you would typically save the user information to a database or a file
        user_data = {
            "username": self.username,
            "email": self.email,
            "password": self.password
        }
        print("User information stored:", user_data)