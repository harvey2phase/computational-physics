from numpy import *
from matplotlib.pyplot import *
from time import *

# Graph the Feigenbaum plot using the basic method in the textbook
def basic():
    r_list, x_list, r, x = [], [], 1, 0.5
    
    # Iterate through r = 1 to r = 4
    while r < 4:
        
        i = 0
        
        # First iterate the logistic map equation 1000 times
        while i < 1000:
            x = r * x * (1 - x)
            i += 1

        # Iterate the logistic map another 1000 times then plot
        while i < 2000:
            x = r * x * (1 - x)
            r_list.append(r)
            x_list.append(x)
            i += 1
            
        r += 0.01
        
    scatter(r_list, x_list, s = 0.1)

# Graph the Feigenbaum plot using the approach described in footnote 10
def footnote_10():
    # Create two arrays of the same length, each containing r and x
    r = linspace(1.0, 4.0, 301)
    x = full(301, 0.5)
    
    # First iterate the logistic map equation 1000 times
    for i in range(1000):
        x = r * x * (1 - x)
        
    # Iterate the logistic map another 1000 times then plot
    for i in range(1000):
        x = r * x * (1 - x)
        scatter(r, x, s = 0.1)

# Run both functions and print out the time it takes to compute each
start_time = time()
footnote_10()
end_time_1 = time()
basic()
end_time_2 = time()
print("The basic approach:", end_time_1 - start_time)
print("The footnote approach:", end_time_2 - end_time_1)
