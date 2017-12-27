# Name: Harvey Wang
# B00:  B00726196
# Date: Oct. 18, 2017

# Assignment 3 -- This program defines a function, estimates the integral of the function with various values of N using Riemann sum, then estimates the integral using Monte Carlo method, and plots the result

import math as m
import time as t
import matplotlib.pyplot as plt
import random as r

# Define the function g we're investigating
def g(x):
    return m.sqrt(1 - x ** 2)

# Calculate the integral of function f with N using Reimann sum
def riemann(f, N):
    h = 2 / N
    s = 0

    # Loop through [k, N] to simulate the Sigma function
    for k in range(N):
        x = -1 + h * (k + 1)
        y = f(x)
        s += h * y

    return s

# Configure graph settings and show it
def configure_graph():
    plt.title("N vs. Integral of f(x)")
    plt.xlabel("N")
    plt.ylabel("Integral of f(x)")
    plt.xscale("log", basex = 2)
    plt.yscale("log", basey = 2)
    plt.legend((a, b), ('Riemann', 'Monte Carlo'))
    plt.show()

# Calculate the integral of g(x) using Monte Carlo method
def monte_carlo(n):
    R = 1
    under = 0

    # Create n random points and append them to the list
    for j in range(n):
        x = r.uniform(-R, R)
        y = r.uniform(0, R)

        # check if the new point is under the function g(x)
        if g(x) >= y:
            under += 1

    f = under / n
    A = 2 * (R ** 2) * f

    return A

# Evaluate the integral with N = 100
print("N = 100:", riemann(g, 100))

# Increase N to as large as possible in one second
end = t.time() + 1
i = 1
while t.time() < end:
    a = plt.scatter(i, riemann(g, i), s = 5, c = "g")
    i *= 2

# Show results
print("Most accurate value in one second:", riemann(g, int(i / 2)))

# Increase the number of spheres to as large as possible in one second
end = t.time() + 1
i = 1
while t.time() < end:
    b = plt.scatter(i, monte_carlo(i), s = 5, c = "b")
    i *= 2

configure_graph()
