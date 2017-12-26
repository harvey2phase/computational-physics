# recursive function to find the factorial of x
def fact(x):
    if x == 1:
        return 1
    return x * fact(x - 1)

# recursive function to evaluate e^x using power series
# the precision variable is the number of time the function will sum the series
def powS(x, precision):
    if precision == 0:
        return 1
    return (x ** precision) / fact(precision) + powS(x, precision - 1)

def close_enough(x1, x2):
    if abs(x1 - x2) < accuracy:
        return True
    return False

def myexp(x):
    sum1 = powS(x, 1)
    sum2 = powS(x, 2)
    i = 3
    # "keep adding terms until they no longer change the result"
    while not close_enough(sum1, sum2):
        sum1 = sum2
        sum2 = powS(x, i)
        i += 1
    return sum2

accuracy = 10 ** -7

# print e^i where i is 0 to 20
for i in range(20):
    print(myexp(i))
