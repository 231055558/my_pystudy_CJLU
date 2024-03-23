from sklearn.datasets import load_boston
def load_data():
    data = load_boston()
    x = data.data
    y = data.target
    print(x)
    print(y)
    return x,y
load_boston()