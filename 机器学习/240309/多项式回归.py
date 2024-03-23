from sklearn.preprocessing import PolynomialFeatures
import numpy as np
from sklearn.linear_model import LinearRegression
# a = [[3,4],[2,3]]
# model = PolynomialFeatures(degree=2,include_bias=False)
# b = model.fit_transform(a)
# print(b)

def make_data():
    np.random.seed(10)
    x1 = np.random.randint(5,10,50).reshape(50,1)
    x2 = np.random.randint(5,16,50).reshape(50,1)
    x,y = np.hstack((x1,x2)),0.5*(x1+x2)*x1
    return x,y

def train(x,y):
    poly = PolynomialFeatures(degree=2,include_bias=False)
    x_mul = poly.fit_transform(x)
    model = LinearRegression()
    model.fit(x_mul,y)
    print("权重分布：",model.coef_)
    print("偏置量：",model.intercept_)

if __name__ == '__main__':
    x,y = make_data()
    train(x,y)
