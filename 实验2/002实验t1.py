my_list = [int(x) for x in input().split()]
a=0
while a<=4:
    for i in range(4,a,-1):
        if my_list[i]>my_list[i-1]:
            my_list[i],my_list[i-1]=my_list[i-1],my_list[i]
        else:
            my_list[i], my_list[i - 1] = my_list[i], my_list[i-1]
    print(my_list[a],end=' ')
    a+=1