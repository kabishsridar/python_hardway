class Student(object):
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
    def display_data(self):
        print(self.name)
        print(self.colour)
st1 = Student("kamal", "red")
print(st1.name)