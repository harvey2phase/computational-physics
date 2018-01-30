import numpy as np
import random as ran
import matplotlib.pyplot as plt

# Returns True if (x, y) is within bounds
def inBounds(x, y):
    if x > 511 or x < 0 or y > 1023 or y < 0:
        return False
    return True

# Returns True if (x, y) is a local max
def localMax(x, y):
    for i in values:
        if alts[x, y] < values[i]:
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
        s[key] = alts[s[key]]

    return s

# Returns (x, y) of the step to take
# (A greedy algorithm to find the next step to take)
def maxStep(x, y):
    step = max(values, key=values.get)
    return adjacentCoors(x, y)[step]

alts = np.loadtxt('altitude.txt')
width, height = len(alts[0]), len(alts)
X, Y = [], []
N = 10 ** 4
for i in range(N):
    x, y = ran.randint(0, height-1), ran.randint(0, width-1)
    values = adjacentValues(x, y)

    while not localMax(x, y):
        x, y = maxStep(x, y)
        values = adjacentValues(x, y)

    X.append(x)
    Y.append(y)

plt.gray()
plt.imshow(alts)
plt.scatter(Y, X, c='g', s=1)
plt.title('Local Maximums on World Map with 10,000 Random Points')
plt.show()
