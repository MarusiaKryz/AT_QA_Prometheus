class User:
    def __init__(self, name = None, second_name = None):
        self.name = name
        self.second_name = second_name

    def create(self):
        self.name = 'Mariia'
        self.second_name = 'Kryzhalko'

    def remove(self):    
        self.name = ''
        self.second_name = ''
