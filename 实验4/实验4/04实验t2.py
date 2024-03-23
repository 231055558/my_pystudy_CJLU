class TicketingMachine:
    film = {}

    def __init__(self):
        pass
    def addFilm(self,name,maxseat,price):
        self.film[name]=[0,maxseat,price]
    def book(self,name,count):
        if name not in self.film.keys():
            print("无此电影\n")
            return False
        if self.film[name][0]+count>self.film[name][1]:
            print("座位已满\n")
            return False
        self.film[name][0] += count
        return True
    def cancel(self,name,count):
        if name not in self.film.keys():
            print("无此电影\n")
            return False
        if self.film[name][0]-count<0:
            print("退票数量大于已售数量\n")
            return False
        self.film[name][0] -= count
        return True
    def box_office(self):
        sump=0
        for i in self.film:
            sump += self.film[i][0]*self.film[i][2]
        return sump

f=0
t=TicketingMachine()
while True:
    print("\n输入1:录入新上映电影"
           "\n输入2:预定电影票"
           "\n输入3:电影票退票"
           "\n输入4:显示当前总票房"
            "\n输入5:结束程序\n")
    n=input()
    if n == "1" :
        while f == 0 :
            try:
                name=input("请输入电影名称：")
                maxseat=input("请输入最大座位数：")
                price=input("请输入票价：")
                t.addFilm(name,int(maxseat),int(price))
                f=1
            except:
                print("输入格式有误，请重新输入\n")
                f=0
        f = 0
    elif n == "2" :
        while f == 0:
            try:
                name=input("请输入电影名称：")
                count=input("请输入购票数量：")
                if t.book(name, int(count)):
                    print("购票成功\n")
                f = 1
            except:
                print("输入格式有误，请重新输入\n")
                f = 0
        f = 0
    elif n == "3" :
        while f == 0:
            try:
                name=input("请输入电影名称：")
                count=input("请输入退票数量：")
                if t.cancel(name, int(count)):
                    print(" 退票成功\n")
                f = 1
            except:
                print("输入格式有误，请重新输入\n")
                f = 0
        f = 0
    elif n == "4" :
        sump=t.box_office()
        print("总票房是：",sump)
    elif n == "5" :
        break
    else:
        print("输入错误，请重新输入\n")
        continue

















