import numpy as np
from math import e
import matplotlib.pyplot as plt

def triangular(i, a, m, b):
    y = list()
    for x in i:
        y.append(max(min((x - a)/(m - a), (b - x)/(b - m)), 0))
    return y

def trapezoidal(i, a, m, n, b):
    y = list()
    for x in i:
        y.append(max(min((x - a)/(m - a), 1,(b - x)/(b - n)), 0))
    return y

# def gaussianaSlide(x, k, m):
#     return e**(-k*(x - m)**2)

def gaussiana(i, k ,m):
    y = list()
    k = k/2
    for x in i:
        y.append(e**((-(x - m)**2)/(k**2)))
    return y

def zadeh(a):
    y = list()
    for i in np.arange(0, len(a), 1):
        y.append(1 - a[i])
    return y

def sugeno(a, s):
    y = list()
    for i in np.arange(0, len(a), 1):
        y.append((1 - a[i])/(1 + s*a[i]))
    return y

def yager(a, w):
    y = list()
    for i in np.arange(0, len(a), 1):
        y.append((1 - a[i]**w)**(1/w))
    return y

def somaProbabilistica(a, b):
    y = list()
    for i in np.arange(0, len(a), 1):
        y.append((a[i] + b[i]) - (a[i]*b[i]))
    return y

def somaLimitada(a, b):
    y = list()
    for i in np.arange(0, len(a), 1):
        y.append(min(a[i]+b[i],1))
    return y

def somaDrastica(a, b):
    y = list()
    for i in np.arange(0, len(a), 1):
        if b[i] == 0:
            y.append(a[i])
        elif a[i] == 0:
            y.append(b[i])
        else:
            y.append(1)
    return y


def produto(a, b):
    y = list()
    for i in np.arange(0, len(a), 1):
        y.append(a[i]*b[i])
    return y

def produtoLimitado(a, b):
    y = list()
    for i in np.arange(0, len(a), 1):
        y.append(max(0, (a[i]+b[i])-1))
    return y

def produtoDrastico(a, b):
    y = list()
    for i in np.arange(0, len(a), 1):
        if a[i] == 1:
            y.append(b[i])
        elif b[i] == 1:
            y.append(a[i])
        else:
            y.append(0)
    return y

def maximo(a, b):
    y = list()
    for i in np.arange(0, len(a), 1):
        y.append(max(a[i], b[i]))
    return y

def minimo(a, b):
    y = list()
    for i in np.arange(0, len(a), 1):
        y.append(min(a[i], b[i]))
    return y

def cog(x, a):
    prod = np.sum(a * x)
    sum = np.sum(a)
    return prod/sum


### MAMDANI
ante = list()
cons = list()

x = np.linspace(-10, 10, 100, False)
y = np.linspace(0, 10, 100, False)


ante.append(trapezoidal(x, -20, -15, -6, -3))
ante.append(trapezoidal(x, -6, -3, 3, 6))
ante.append(trapezoidal(x, 3, 6, 15, 20))

cons.append(trapezoidal(y, -2.46, -1.46, 1.46, 2.46))
cons.append(trapezoidal(y, 1.46, 2.46, 5, 7))
cons.append(trapezoidal(y, 5, 7, 13, 15))

b1 = minimo(ante[2], cons[2])
b2 = minimo(ante[1], cons[1])
b3 = minimo(ante[0], cons[0])

out = maximo(maximo(b1, b2), b3)

# plt.figure(1)
# plt.ylim(0, 2)
# plt.plot(x, ante[0])
# plt.plot(x, ante[1])
# plt.plot(x, ante[2])
# plt.figure(2)
# plt.ylim(0, 2)
# plt.plot(y, cons[0])
# plt.plot(y, cons[1])
# plt.plot(y, cons[2])
# plt.show()
