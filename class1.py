#class1.py
class Person:
    def __init__(self):
        self.name = "default name"
    def print(self):
        print("My name is {0}".format(self.name))

p1 = Person()
p2 = Person()
p1.print()
p2.print()

Person.title = "new title"
print(p1.title)
print(p2.title)
print(Person.title)

p1.age=30
print(p1.age)
#print(p2.age)
