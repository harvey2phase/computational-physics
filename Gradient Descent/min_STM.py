import numpy as np
import random as ran
import matplotlib.pyplot as plt

# Returns True if (x, y) is within bounds
def inBounds(x, y):
    if x > height-1 or x < 0 or y > width-1 or y < 0:
        return False
    return True

# Returns True if (x, y) is a local max
def localMin(x, y):
    for i in values:
        if stms[x, y] > values[i]:
            return False
    return True

# Return a dict. of (x, y) containing surrounding points
def adjacentCoors(x, y):
    s = {
        0: (x, y + 1),
        1: (x, y - 1),
        2: (x + 1, y),
        3: (x - 1, y),
        4: (x + 1, y + 1),
        5: (x + 1, y - 1),
        6: (x - 1, y + 1),
        7: (x - 1, y - 1)
    }
    rmKeys = []
    for key in s:
        xx, yy = s[key]
        if not inBounds(xx, yy):
            rmKeys.append(key)
    for key in rmKeys:
        if key in s:
            del s[key]
    return s

# Returns a dict. of floats containing surrounding alt. values
def adjacentValues(x, y):
    s = adjacentCoors(x, y)
    for key in s:
        s[key] = stms[s[key]]
    return s

# Returns (x, y) of the step to take
# (A greedy algorithm to find the next step to take)
def minStep(x, y):
    step = min(values, key=values.get)
    return adjacentCoors(x, y)[step]

stms = np.loadtxt('stm.txt')
width, height = len(stms[0]), len(stms)
X, Y = [], []
N = 10 * 4
for i in range(N):
    x, y = ran.randint(0, height-1), ran.randint(0, width-1)
    values = adjacentValues(x, y)

    while not localMin(x, y):
        x, y = minStep(x, y)
        values = adjacentValues(x, y)

    X.append(x)
    Y.append(y)

plt.imshow(stms)
plt.scatter(Y, X, c='r', s=1)
plt.axis('off')
plt.title('Minimums with 10,000 random points')
plt.show()
