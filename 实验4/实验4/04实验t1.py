class Person:
    def __init__(self,name):
        self.name=name
    def get_name(self):
        return self.name
me=Person("Li_Haoyang")
print(me.get_name())