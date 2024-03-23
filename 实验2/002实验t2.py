dict_xs={'001':19,'002':91,'003':61,'004':13,'005':7,'006':18,'007':99,'008':100,'009':98,'010':96}
a=input("需要查询：")
n=0

if a=="平均分":
    for i in range(1,11):
        name = '%03d' % i
        n += dict_xs[name]
    print("平均分是：",n/10)

elif a=="最高分":
    n=0
    for i in range(1,11):
        name = '%03d' % i
        if dict_xs[name]>n:
            n=dict_xs[name]
            maxname=name
    print("最高分是",maxname,"得了",n)
elif a=="最低分":
    n = 100
    for i in range(1, 11):
        name = '%03d' % i
        if dict_xs[name] < n:
            n = dict_xs[name]
            minname = name
    print("最低分是", minname, "得了", n)

else:
    try:
        print(a,"的分数是",dict_xs[a])
    except:
        print("你输的啥玩意")