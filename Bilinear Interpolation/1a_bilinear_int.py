import numpy as np
import matplotlib.pyplot as plt

# A bilinear interpolating function
def f(x, y):
    F11 = x * y * f11
    F00 = (1 - x) * (1 - y) * f00
    F10 = x * (1 - y) * f10
    F01 = (1 - x) * y * f01
    return F11 + F00 + F10 + F01

def annotate():
    plt.annotate(s = f00, fontsize = 10, xy = (1, 1))
    plt.annotate(s = f01, fontsize = 10, xy = (N-1, 1))
    plt.annotate(s = f10, fontsize = 10, xy = (1, N-1))
    plt.annotate(s = f11, fontsize = 10, xy = (N-1, N-1))

# Creating two arrays from x0=y0=0 to x1=y1=1 with N points and setting the corner values
N = 10 ** 3
X, Y = np.linspace(0, 1, N), np.linspace(0, 1, N)
interps = np.empty([N, N])
f00, f01, f10, f11 = 0.5, 1, -1, 2

x = 0
for i in X:
    y = 0
    for j in Y:
        interps[x][y] = f(i, j)
        y += 1
    x += 1

plt.imshow(interps)
plt.jet()
plt.axis('off')
plt.title('Bilinear interpolation with 0.5, 1, -1, 2')
annotate()
plt.show()
