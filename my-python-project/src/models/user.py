class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def validate(self):
        if not self.username or not self.email or not self.password:
            return False
        if "@" not in self.email:
            return False
        return True

    def save(self):
        if self.validate():
            # Here you would add code to save the user data to a database or file
            return True
        return False