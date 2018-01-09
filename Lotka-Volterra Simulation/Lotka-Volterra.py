import numpy as np
import matplotlib.pyplot as plt

# The Lotka-Volterra
def f(r, t):
    alpha, beta, gamma, delta = 1, 0.5, 0.5, 2
    x = r[0]
    y = r[1]
    fx = alpha * x - beta * x * y
    fy = gamma * x * y - delta * y
    return np.array([fx, fy], float)

# Runge Kutta 4th Order
def rk4(f, r, a, b, N):
    h = (b - a) / N
    t_points = np.arange(a, b, h)
    x_points, y_points = [], []

    for t in t_points:
        x_points.append(r[0])
        y_points.append(r[1])
        k1 = h * f(r, t)
        k2 = h * f(r + k1/2, t + h/2)
        k3 = h * f(r + k2/2, t + h/2)
        k4 = h * f(r + k3, t + h)
        r += (k1 + 2*k2 + 2*k3 + k4) / 6

    return x_points, y_points, t_points

# Euler's Method
def euler(f, r, a, b, N):
    h = (b - a) / N
    t_points = np.arange(a, b, h)
    x_points, y_points = [], []

    for t in t_points:
        x_points.append(r[0])
        y_points.append(r[1])
        r += h * f(r, t)

    return x_points, y_points, t_points

def plot_function_of_time():
    # Plotting with RK4
    R_X, R_Y, T = rk4(f, r, a, b, N)
    plt.figure(1)
    plt.title('Lotka-Volterra with RK4; N = ' + str(N))
    plt.plot(T, R_X, label='Population of rabits')
    plt.plot(T, R_Y, label='Population of foxes')
    plt.xlabel('time')
    plt.legend()
    plt.savefig('Output Graphs/Function of Time/' + str(N) + ' RK4.png')
    plt.clf()

    # Plotting with Euler
    E_X, E_Y, T = euler(f, r, a, b, N)
    plt.figure(2)
    plt.title('Lotka-Volterra with Euler\'s Method; N = ' + str(N))
    plt.plot(T, E_X, label='Population of rabits')
    plt.plot(T, E_Y, label='Population of foxes')
    plt.xlabel('time')
    plt.legend()
    plt.savefig('Output Graphs/Function of Time/' + str(N) + ' Euler.png')
    plt.clf()

    # Plotting the difference
    D_X, D_Y = [], []
    for i in range(len(T)):
        D_X.append(abs(R_X[i] - E_X[i]))
        D_Y.append(abs(R_Y[i] - E_Y[i]))
    plt.figure(3)
    plt.title('Differeces between RK4 and Euler; N = ' + str(N))
    plt.plot(T, D_X, label='Population of rabits')
    plt.plot(T, D_Y, label='Population of foxes')
    plt.xlabel('time')
    plt.legend()
    plt.savefig('Output Graphs/Function of Time/' + str(N) + ' Diff.png')
    plt.clf()
x, y = 2, 2
r = np.array([x, y], float)
a, b = 0, 30

for i in np.arange(3, 7):
    N = 10 ** i
    plot_function_of_time()

# Plot as a function of timestep at t = 15
b = 15
N = 1000
D_X, D_Y, D_N = [], [], []
while N < 100000:
    R_X, R_Y, T = rk4(f, r, a, b, N)
    E_X, E_Y, T = euler(f, r, a, b, N)
    D_X.append(abs(R_X[len(R_X)-1] - E_X[len(E_X)-1]))
    D_Y.append(abs(R_Y[len(R_Y)-1] - E_Y[len(E_Y)-1]))
    D_N.append(N)
    N *= 2

plt.figure(4)
plt.title('Differce between RK4 and Euler as function of time steps at t = 15')
plt.plot(D_N, D_X, label='Population of rabits')
plt.plot(D_N, D_Y, label='Population of foxes')
plt.xlabel('N')
plt.legend()
plt.savefig('Output Graphs/Function of N.png')
