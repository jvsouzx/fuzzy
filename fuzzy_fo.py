import numpy as np
from math import e
import matplotlib.pyplot as plt

def triangular(x, a, m, b):
    return max(min((x - a)/(m - a), (b - x)/(b - m)), 0) 

def trapezoidal(x, a, m, n, b):
    return max(min((x - a)/(m - a), 1,(b - x)/(b - n)), 0)

def gaussiana(x, k, m):
    return e**(-k*(x - m)**2)

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
    for i in np.arange(0, max(len(a), len(b)), 1):
        y.append((a[i] + b[i]) - (a[i]*b[i]))
    return y

def somaLimitada(a, b):
    y = list()
    for i in np.arange(0, max(len(a), len(b)), 1):
        y.append(min(a[i]+b[i],1))
    return y

def somaDrastica(a, b):
    y = list()
    for i in np.arange(0, max(len(a), len(b)), 1):
        if b[i] == 0:
            y.append(a[i])
        elif a[i] == 0:
            y.append(b[i])
        else:
            y.append(1)
    return y

def produto(a, b):
    y = list()
    for i in np.arange(0, max(len(a), len(b)), 1):
        y.append(a[i]*b[i])
    return y

def produtoLimitado(a, b):
    y = list()
    for i in np.arange(0, max(len(a), len(b)), 1):
        y.append(max(0, (a[i]+b[i])-1))
    return y

def produtoDrastico(a, b):
    y = list()
    for i in np.arange(0, max(len(a), len(b)), 1):
        if b[i] == 1:
            y.append(a[i])
        elif a[i] == 1:
            y.append(b[i])
        else:
            y.append(0)
    return y

def maximo(a, b):
    y = list()
    for i in np.arange(0, max(len(a), len(b)), 1):
        y.append(max(a[i], b[i]))
    return y

def minimo(a, b):
    y = list()
    for i in np.arange(0 , max(len(a), len(b)), 1):
        y.append(min(a[i], b[i]))
    return y

def main():

    x = list()
    y = list()

    for i in np.arange(0, 9, 1):
        y.append(list())

    for i in np.arange(0, 12, 0.01):
        x.append(i)
        y[0].append(triangular(i, 2, 4, 6))
        y[1].append(triangular(i, 4, 6, 8))
        y[2].append(triangular(i, 6, 8, 10))
        
        y[3].append(trapezoidal(i, 2, 3, 5, 6))
        y[4].append(trapezoidal(i, 4, 5, 7, 8))
        y[5].append(trapezoidal(i, 6, 7, 9, 10))
        
        y[6].append(gaussiana(i, 1, 4))
        y[7].append(gaussiana(i, 1, 6))
        y[8].append(gaussiana(i, 1, 8))

    figure, axis = plt.subplots(3, 1)  
    
    for i in np.arange(0, 3, 1):
        axis[0].plot(x, y[i])
  
    for i in np.arange(3, 6, 1):
        axis[1].plot(x, y[i])
    
    for i in np.arange(6, 9, 1):
        axis[2].plot(x, y[i])

    # Complementos
    fig, axis = plt.subplots(3,1)
    axis[0].plot(x, y[0])
    axis[0].plot(x, zadeh(y[0]))
    axis[2].plot(x, y[0])
    axis[2].plot(x, yager(y[0], 0.6))
    axis[1].plot(x, y[0])
    axis[1].plot(x, sugeno(y[0], 2))

    # União
    fig, axis = plt.subplots(4,1)
    axis[0].plot(x, y[0])
    axis[0].plot(x, y[1])
    axis[0].plot(x, maximo(y[0],y[1]))
    axis[1].plot(x, y[0])
    axis[1].plot(x, y[1])
    axis[1].plot(x, somaProbabilistica(y[0], y[1]))
    axis[2].plot(x, y[0])
    axis[2].plot(x, y[1])
    axis[2].plot(x, somaLimitada(y[0], y[1]))
    axis[3].plot(x, y[0])
    axis[3].plot(x, y[1])
    axis[3].plot(x, somaDrastica(y[0], y[1]))

    # Interseção
    fig, axis = plt.subplots(4,1)
    axis[0].plot(x, y[0])
    axis[0].plot(x, y[1])
    axis[0].plot(x, minimo(y[0],y[1]))
    axis[1].plot(x, y[0])
    axis[1].plot(x, y[1])
    axis[1].plot(x, produto(y[0], y[1]))
    axis[2].plot(x, y[0])
    axis[2].plot(x, y[1])
    axis[2].plot(x, produtoLimitado(y[0], y[1]))
    axis[3].plot(x, y[0])
    axis[3].plot(x, y[1])
    axis[3].plot(x, produtoDrastico(y[0], y[1]))

    plt.show()

main()

