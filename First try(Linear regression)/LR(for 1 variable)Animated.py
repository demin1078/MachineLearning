import matplotlib.pyplot as plt
import functools
import statistics
import math
area = [100,110,115,120,135,170,173,190,220,250]
price = [500, 530, 520, 550, 580,600,590,670,760,850]

def hypothesis(th0,th1,x1):
    return th0 + th1*x1
#It's a derivative, I was wrong
def squareError(m, th0, th1, x, y,x0):
    s = 0
    if x0 == 1:
        x0 = [1 for i in range(m)]
    for i in range(m):
        s += (hypothesis(th0, th1, x[i]) - y[i]) * x0[i]
    return s/(2*m)
def createLine(th0,th1,m):
    c = m.copy()
    arr = [th0+th1*i for i in c]
    plt.plot(area,arr)
    plt.show()

th0 = 0
th1 = 0
a = 0.0001
m = len(price)
th0Past = 1000000
th1Past = 1000000
it = 0
while abs(th1 - th1Past) > 0.00000001 and abs(th0 - th0Past) > 0.00000001:
    th0Past = th0
    th1Past = th1

    temp0 = th0 - a * squareError(m,th0,th1,area,price,1)
    temp1 = th1 - a * squareError(m,th0,th1,area,price,area)
    th0 = temp0
    th1 = temp1
    #print(th0,th1)
    it += 1

    if it % 5000 == 0:
        x_values = area
        y_values = [th0 + th1 * i for i in area]
        plt.xlim(0,300)
        plt.ylim(0,1000)
        print(th0,th1,it)
        plt.cla()
        plt.scatter(area,price)
        plt.plot(x_values, y_values)
        plt.pause(0.0001)
plt.show()
print(th0,th1,it)
#createLine(th0,th1,area)


