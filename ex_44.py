class Parent(object):
    def overrride(self):
        print("PARENT override()")
    def implicit(self):
        print("PARENT implicit()")
    def altered(self):
        print("PARENT altered()")
class Child(Parent):
    def __init__(self, stuff):
        self.stuff = stuff
        super(Child, self).__init__()
    def override(self):
        print("CHILD override()")
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.overrride()
son.overrride()

dad.altered()
son.altered()