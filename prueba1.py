import numpy as np

x = [1,2,3,4,5,6,7,8,9,10]
y = [2,4,5,4,5,7,8,9,10,12]

def linear_regression(x,y):
    x = np.array(x)
    y = np.array(y)

    m, b = np.polyfit(x,y,1)
    return m,b


