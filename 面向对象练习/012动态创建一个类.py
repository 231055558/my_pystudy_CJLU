# class Person:
#     def __init__(self):
#         pass
# print(type(Person))#type类

def __init__(self,name):
    self.name = name
dog_class = type("Dog",(object,),{"role":"dog","__init__":__init__})#init只能写在上面
# print(dog_class)
# print(type(dog_class))
# print(dog_class.role)
# dog1 = dog_class
# print(dog1.role)


d = dog_class("Tim")
print(d.role,d.name)