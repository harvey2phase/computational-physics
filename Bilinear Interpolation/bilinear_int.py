import numpy as np
import matplotlib.pyplot as plt

# Setting the four corner values
f00, f01, f10, f11 = 3.14, -6, -2, 4

# Setting x0=y0=0 and x1=y1=1 yields u=x and v=y
# Therefore, f can be simplified to:
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

# Determine if the input is close enough to zero
def close_to_zero(x):
    if abs(x) < 10 ** -3:
        return True
    return False

# "Normal" binary search, where negative numbers are on the left side
def n_to_p(L, l, m, h):
    if close_to_zero(L[m]):
        return m

    # If L has been searched through
    elif h <= l:
        return 0

    # Search right side
    elif L[m] < 0:
        if m == int((h-m)/2) + m:
            return 0
        return n_to_p(L, m, int((h-m)/2) + m, h)

    # Search left side
    else:
        if m == int((m-l)/2) + l:
            return 0
        return n_to_p(L, l, int((m-l)/2) + l, m)

# Binary search with positive numbers on the left side
def p_to_n(L, l, m, h):
    if close_to_zero(L[m]):
        return m

    # If L has been searched through
    elif h <= l:
        return 0

    # Search left side
    elif L[m] < 0:
        if m == int((m-l)/2) + m:
            return 0
        return p_to_n(L, l, int((m-l)/2) + l, m)
    else:
        if m == int((h-m)/2) + l:
            return 0
        return p_to_n(L, m, int((h-m)/2) + m, h)

# Creating two arrays from x0=y0=0 to x1=y1=1 with N points
N = 1000
X, Y = np.linspace(0, 1, N), np.linspace(0, 1, N)
inters, zero_line = np.empty([N, N]), []

x = 0
for i in X:
    y = 0
    for j in Y:
        inters[x][y] = f(i, j)
        y += 1
    # List goes small to large
    if inters[x][N-1] > inters[x][0]:
        zero_line.append(n_to_p(inters[x], 0, int(N / 2), N))
    else:
        zero_line.append(p_to_n(inters[x], 0, int(N / 2), N))

    x += 1

plt.imshow(inters)
plt.jet()
plt.scatter(zero_line, np.linspace(0, N-1, N), s = 0.1, c = 'k')
plt.axis('off')
annotate()
plt.show()
