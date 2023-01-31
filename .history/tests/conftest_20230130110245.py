class User:
    def __init__(self, name = None, second_name = None):
        self.name = name
        self.second_name = second_name

    def create(self):
        self.name = input("Enter your name")
        self.second_name = input("Enter your last name")

