def text17():
    j = 2
    while j < 100 :
        flag = 0
        i = 2
        while i < j :
            if j % i == 0 :
                flag = 1
                break
            i += 1
        if flag == 0:
            print(i)
        j += 1
text17()