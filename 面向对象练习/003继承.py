# class Animal:
#     a = "a"
#     def __init__(self,name):
#         self.name = name
#         print("你好")
#     def eat(self):
#         print(self.name,"eat")
#
# class Person(Animal):
#     def talk(self,text):
#         print("person %s is talking %s" % (self.name, text))
#     def eat(self):
#         print(self.name,"not eat")
#
# class Dog(Animal):
#     pass
#
# p = Person("Tim")
# print(p.a)
# p.eat()


#
# class Animal:
#     def __init__(self,name):
#         self.name = name
#         print("你好",self.name)
#     def eat(self):
#         print(self.name,"eat")
#
# class Person(Animal):
#     def __init__(self, name, hobby):
#         #Animal.__init__(self,name) # 比较少用，多用super语法
#         #super(Person,self).__init__(name) # 语法效果同上，py3通常如此使用
#         super().__init__(name) # 语法效果同样同上，更加简便
#         self.hobby = hobby
#     def talk(self,text):
#         print("person %s is talking %s" % (self.name, text))
#     def eat(self):
#         print(self.name,"not eat")
#
# class Dog(Animal):
#     pass
#
# p = Person("Tim","shit")

#
#
# class ShenXian:
#     def fly(self):
#         print("can fly")
#     def play(self):
#         print("cant play")
#
# class Monkey:
#     def play(self):
#         print("can play")
#
# class MonkeyKing(Monkey,ShenXian):
#     def play_goden_stick(self):
#         print("play_goden_stick")
#
# m = MonkeyKing()
# m.play()

# class A:#6
#     # def test(self):
#     #     print("A")
#     pass
# class B(A):#3
#     # def test(self):
#     #     print("B")
#     pass
# class B2:#7
#     # def test(self):
#     #     print("B2")
#     pass
# class C(A):#5
#     # def test(self):
#     #     print("C")
#     pass
# class C2:#8
#     # def test(self):
#     #     print("C2")
#     pass
# class D(B,B2):#2
#     # def test(self):
#     #     print("D")
#     pass
# class E(C,C2):#4
#     # def test(self):
#     #     print("E")
#     pass
# class F(D,E):#1
#     # def test(self):
#     #     print("F")
#     pass
# i = F()
# print(F.mro())



