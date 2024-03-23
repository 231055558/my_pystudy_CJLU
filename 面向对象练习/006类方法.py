# class Dog:
#     def __init__(self,name):
#         self.name = name
#     @classmethod
#     def eat(self):
#         print(self)
#         print("dog %s eat" % self.name)
# d = Dog("lx")
# Dog.name = 'sd'
# d.eat()

# class Stu:
#     stu_num = 0
#     def __init__(self,name):
#         self.name = name
#         self.stu_num += 1
#         print("学生总数：",self.stu_num)
#
# s1 = Stu("haha")
# s2 = Stu("shit")
# s3 = Stu("mama")
# #  发现这样不行啊，只是单纯对实例变量赋值

# class Stu:
#     __stu_num = 0
#     def __init__(self,name):
#         self.name = name
#         self.add()
#
#     @classmethod
#     def add(cls):
#         cls.__stu_num += 1
#         print("学生总数：",cls.__stu_num)
#
# s1 = Stu("haha")
# s2 = Stu("shit")
# s3 = Stu("mama")

class Student:
    def __init__(self,name):
        self.name = name

    @property
    def fly(self):
        print(self.name,"flying")

s = Student("jack")
s.fly