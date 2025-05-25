class Animal(object): # set animal as an object
    pass
class Dog(Animal): # set dog is an animal
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Dog named {self.name}"
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

rover = Dog("Rover")
satan = Cat("Satan")
mary = Person("Mary")
mary.pet = satan

# display rover
print(rover)
