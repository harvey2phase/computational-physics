# Name: Harvey Wang
# B00:  B00726196
# Date: Oct. 18, 2017

# Assignment 3 -- This program defines a function then calculates its derivative with delta = 10 ^ -2

# Define the function g we're investigating
def g(x):
    return x * (x - 1)

# Calculate the derivative of function f at x with delta
def derivative(f, x, delta):
    return (f(x + delta) - f(x)) / delta

print(derivative(g, 1, 10 ** -2))
