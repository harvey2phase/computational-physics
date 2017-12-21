import math as m

# a recursive function to find the square root of x
def sqrt_re(x, m, mid, M): 
    # base case
    if M - m < accuracy:
        return mid 
    if mid ** 2 == x:
        return mid
    # choose the left side of the range
    elif mid ** 2 > x:
        return sqrt_re(x, m, (mid - m) / 2 + m, mid)
    # choose the right side of the range
    else:
        return sqrt_re(x, mid, (M - mid) / 2 + mid, M)

def sqrt(x):
    return sqrt_re(x, 1, x / 2, x)

x = 5
accuracy = 10 ** -6

my_sqrt = sqrt(x)
math_sqrt = m.sqrt(x)
error = abs(my_sqrt - math_sqrt)

print('x:\t\t', x)
print('Accuracy:\t', accuracy)
print('My sqrt:\t', my_sqrt)
print('Math sqrt:\t', math_sqrt)
print('Error:\t\t', error)