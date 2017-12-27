# Name: Harvey Wang
# B00:  B00726196
# Date: Oct. 18, 2017

# Assignment 3 -- This This program defines a function then calculates its derivative with various values of delta

# Define the function f(x)
def f(x):
    return x * (x - 1)

# Calculate the derivative of function f at x with delta
def derivative(f, x, delta):
    return (f(x + delta) - f(x)) / delta

i = -2
while i >= -14:
    print(i, derivative(f, 1, 10 ** i))
    i -= 2
