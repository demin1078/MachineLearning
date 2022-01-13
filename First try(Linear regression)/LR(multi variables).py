import numpy as np
import math
import matplotlib.pyplot as plt
def priceCost(x, y, theta,m):
    return math.sqrt((sum((np.dot(x,theta) - y)**2)/(2*m)))


def gradientDescent(a, it, x,y, theta, n,m):
    for _ in range(it):
        newTheta = []
        for i in range(n):
            newTheta.append((np.dot(x[:, i], np.dot(x, theta) - y))[0] * (1/(m*n)))
        theta = theta.transpose() - a * np.array([newTheta])
        theta = theta.transpose()

    return theta


# Step of descent
a = 0.1

# Add features
areaStart = [] # features
priceStart = [] # results
file = open("ex1data2.txt")
b = [1]
for line in file:
    arr = list(map(float,line.split(",")))
    arr = b + arr
    areaStart.append(arr[:-1])
    priceStart.append(arr[-1])

n = len(arr) - 1
area = np.array(areaStart)

price = np.array([priceStart]).transpose()
X = area
m = price.shape[0]  # Number of examples

theta = np.array([[0 for i in range(n)]]).transpose()


#Normalization
mu1 = (max(X[:,1]) - min(X[:,1]))
mu2 = (max(X[:,2]) - min(X[:,2]))
X[:,1] = (X[:,1]) / (max(X[:,1]) - min(X[:,1]))
X[:,2] = (X[:,2]) / (max(X[:,2]) - min(X[:,2]))

print(X)

# use Gradient descent
iterat = 1500000
theta = gradientDescent(a, iterat, X, price, theta, n, m)

theta[1][0] = theta[1][0]/mu1
theta[2][0] = theta[2][0]/mu2
print(theta)
print(priceCost(X, price, theta, m))
print("---")

