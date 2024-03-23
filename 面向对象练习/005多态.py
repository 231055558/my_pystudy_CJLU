class Dog:
    def __init__(self,name):
        self.type = "Dog"
        self.name = name
class Cat:
    def __init__(self,name):
        self.type  = "Cat"
        self.name = name
class Person:
    def __init__(self,name):
        self.type = "Person"
        self.name = name
def choose(animal_obj):
    print(animal_obj.type)

p = Person("liang")
choose(p)