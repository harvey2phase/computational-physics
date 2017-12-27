from numpy import *
from matplotlib.pyplot import *
from time import *

# Graph the Feigenbaum plot using the approach described in footnote 10
def footnote_10(n):

    # Create two arrays of the same length, each containing r and x
    r = linspace(1.0, 4.0, 301)
    x = full(301, 0.5)
    
    # First iterate the logistic map equation n times
    for i in range(n):
        x = r * x * (1 - x)
        
    # Iterate the logistic map another n times then plot
    for i in range(n * 2):
        x = r * x * (1 - x)
        scatter(r, x, s = 0.1)

    xlabel("r")
    ylabel("x")

# Plot 100, 1000, 100000 iterations and print the time required

time_0 = time()
figure(1)
footnote_10(100)
title("Feigenbaum Plot - 100 Iterations")

time_1 = time()
figure(2)
footnote_10(1000)
title("Feigenbaum Plot - 1000 Iterations")

time_2 = time()
figure(3)
footnote_10(10000)
title("Feigenbaum Plot - 10000 Iterations")

time_3 = time()

print("100 Iterations:  ", time_1 - time_0)
print("1000 Iterations: ", time_2 - time_1)
print("10000 Iterations:", time_3 - time_2)

show()
