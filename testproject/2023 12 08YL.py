import numpy as np
list1 = [1,3,5,7,9]
list2 = [2,4,6,8,10]
# for i in list1 :
#     list2.append(i*i)
# list2 = [i*i for i in list1]
# list2 = [i for i in list1 if i > 5]
# list3 = [list1[i]+list2[i] for i in range(5) ]
# print(list3)

#print(np.array(list1) + np.array(list2))

a = np.arange(1.0,19.0,1.0).reshape(3,6)
b = np.random.rand(6,6) * 3
c = np.ones((6,6))
print(np.dot(a[0:2,-2:],c[0:2,-3:]))#矩阵乘法

