# Name: Harvey Wang
# B00:  B00726196
# Date: Oct. 18, 2017

# Assignment 3 -- This program defines a function, estimate the derivative of the function with various values of delta, and plots the result

import matplotlib.pyplot as plt

# Define the function f(x)
def f(x):
    return x * (x - 1)

# Calculate the derivative of function f at x with delta
def derivative(f, x, delta):
    return (f(x + delta) - f(x)) / delta

# Estimate the derivative with delta 2 ** -1 to 2 ** -16
p = -1
while p > -16:
    plt.scatter(2 ** p, derivative(f, 1, 2 ** p) - 1, s = 5)
    p -= 1

# Show results
plt.title("delta vs. Derivative estimate error")
plt.xlabel("Delta")
plt.ylabel("Error")
plt.xscale("log")
plt.yscale("log")
plt.show()
