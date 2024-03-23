import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#构造数据集
def make_data():
    np.random.seed(20)
    x = np.random.rand(100) * 30 + 50
    noise = np.random.rand(100) * 50
    y = x * 8 - 127 -noise
    return x,y

def main(x,y):
    model = LinearRegression()
    x = np.reshape(x,(-1,1))
    model.fit(np.reshape(x,(-1,1)),y)
    y_pre = model.predict(x)
    print(y_pre)

if __name__ == '__main__':
    x,y = make_data()
    main(x,y)
    print(y)
