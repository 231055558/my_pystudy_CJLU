# class Dog:  #编程规范中，类名首字母大写
#     d_type = "京巴" # 属性，类属性，类变量
#
#     def say_hi(self):   # self 代表实例本身,第一个参数必须是self，def称为一个方法
#         print("hello, i dog, type ",self.d_type)
#
#
# d = Dog() # 生成了一个实例
# d2 = Dog()
#
# d.say_hi()
# d2.say_hi()


class Dog:
    d_type = "京巴" # 公共属性，所有的实例共享
    def __init__(self,name,age): #初始化方法，构造方法，构造函数，实例化时会自动执行，进行初始化工作
        print("nihao",name,age) # 这样并不能保存下两个值
        #想要存下，就需要把值和实例绑定
        self.name = name
        self.age = age

    def say_hi(self):   # self 代表实例本身,第一个参数必须是self，def称为一个方法
        print("hello, i dog, type ",self.d_type,self.name)
d = Dog() # 此时会运行初始化函数
d2 = Dog() #（）中的参数会自动被搬到__init__()中
#self 其实是一个自动传参的过程

Dog.d_type = "藏獒" #一旦修改，所有实例的属性均修改
print(Dog.d_type)
d.say_hi()
d2.say_hi()