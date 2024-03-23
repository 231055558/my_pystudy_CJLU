# class People:
#     nation = "CN"
#     def __init__(self,name,age,sex):
#         ...
#         ...
# p.nation = ...#这样同样可以实现定义一个新的属性

###依赖关系
# class Dog:
#     def __init__(self,master):
#         self.master = master #master是一个对象

###关联关系
# class Person:
#     def __init__(self):
#         self.parter = None # 这里应该指向一个对象，代表另一半
###     #双向关联
# p1.parter = p2
# p2.parter = p1

 ###如果想不需要双向关联就实现绑定和解除，可以单独定一个关系类
# class Relation:
#     def __init__(self,p1,p2):
#         self.couple = [p1,p2]
#         print("[%s]和[%s]确定了关系" % (p1.name, p2.name))
#     def getp(self,p):
#         for i in self.couple:
#             if p == i :
#                 continue
#             else:
#                 return i.name
#         else:
#             print("你没有")
#
#     def Break(self):
#         self.couple.clear()
# class Person:
#     def __init__(self,name):
#         self.name = name
#
# p1 = Person("Liang")
# p2 = Person("Pan")
#
# re = Relation(p1, p2)
#
# re.getp(p1)

#组合关系：

class Dog:
    def __init__(self):
        self.life_val = 100

class Person:
    def __init__(self):
        self.gun = Gun()
class Gun:
    def dog_stick(self,p):
        self.name = "打狗棒"
        self.attack_val = 40
        p.life_val -= self.attack_val
        print(p.life_val)
d = Dog()
p = Person()
p.gun.dog_stick(d)

