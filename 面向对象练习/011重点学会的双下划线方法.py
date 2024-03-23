# class School:
#     def __init__(self,name):
#         self.name = name
#
# p1 = School("Tim")
#
# print(repr(p1))
# print(str(p1))
# print(p1)
# #此时都打印str格式,注意其中print会调用str的方法
#
# class School:
#     def __init__(self,name):
#         self.name = name
#
#     def __repr__(self):
#         return "hello"
#
#     def __str__(self):
#         return "morning"
#
#
# p1 = School("Tim")
# print(repr(p1))     #hello
# print(str(p1))      #morning
# print(p1)           #morning


# class School:
#     def __init__(self,name):
#         self.name = name
#
#     def __del__(self):
#         print(self.name," go shit")
#
# p1 = School("Tim")
# p2 = School("li")
# print("现在还没消失")
# del p1
# print("刚刚消失")
# print("不执行消失，最后也会消失 ")

# class School:
#     def __init__(self,name):
#         self.name = name
#         print("morning")
#         print(self.name)
#     def __new__(cls, *args, **kwargs):
#         print("hahaha")
#         # return School.__init__(cls,"Job")
#         return object.__new__(cls)
#
# p1 = School("Tim")

class School:
    def __init__(self,name):
        self.name = name
        print("good")
    def __call__(self, *args, **kwargs):
        print("hello")

p1 = School("Tim")
p1()#实例名加括号，调用call