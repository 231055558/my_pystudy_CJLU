class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    # def __len__(self):
    #     print("hello")
    #     return 5

    # def __hash__(self):
    #     print("hash")
    #     return 7

    # def __eq__(self, other):
    #     print("hello")
    #     print(other.name)
    #     return 0

    # def __getitem__(self, item):
    #     print("get item 用法的结果：",self.__dict__[item])
    #     print("此时 a 的形式:",self.__dict__)

    def __setitem__(self, key, value):
        print("set item")
        self.__dict__[key] = value

# def len
# p = Person("Tim",19)
# len(p)
# hash(p)

# a = Person("Tim",19)
# b = Person("Lx",15)
# a == b

a = Person("Tim",19)
# a["name"]
a["age1"] = 20
print(a.age1)