class Animal(object): # set animal as an object
    pass
class Dog(Animal): # set dog is an animal
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Dog named {self.name}"
    def name_length(self):
        return f"Length of name is {len(self.name)}"
class Cat(Animal):
    def __init__(self, name):
        self.name = name
class Person(object): # person as an object
    def __init__(self, name):
        self.name = name
        self.pet = None
    def __str__(self):
        return f"Pet named {self.pet}"
class Employee(Person): # employee as a person
    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary
class Fish(object): # fish as a object
    pass
class Salmon(Fish): # salmon as a fish
    pass
class Halibut(Fish):
    pass

name_list = ["Dog1","Dog2","Dog3","Dog4","Dog5","Dog6","Dog7","Dog8","Dog9"]
dog_list = []
for dog in name_list:
    temp = Dog(dog)
    dog_list.append(temp)
# print(len(dog_list[3].name))
print(dog_list[5].name_length())
rover = Dog("Rover")
satan = Cat("Satan")
mary = Person("Mary")
mary.pet = satan

# display rover
print(rover)
print(rover.name)
print(mary.name)