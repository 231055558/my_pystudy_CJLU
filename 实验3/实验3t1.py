from random import randint
x=randint(1,10)
i=1
while i<=3:
    try:
        a=int(input())
        if a>x and a<10:
            print("大了")
        elif a<x and a>0:
            print("小了")
        elif a==x:
            print("对了")
            i=0
            break
        elif a<0 or a>10:
            print("宝贝你猜哪去了，给你机会你不中用啊")
        else :
            print("宝贝你输的啥？")
        i+=1
    except:
        print("宝贝好好输入，生活会陪你演戏，程序和机会不会！")
        i+=1
if i==4:
    print("机会用光了")
