import math as m
import numpy as np
import matplotlib.pyplot as plt

# Function for projectile motion with viscous drag
def f(r, t):
    vx = r[2]
    vz = r[3]

    dx = vx
    dz = vz
    dvx = -eta * vx
    dvz = -g - eta * vz
    return np.array([dx, dz, dvx, dvz], float)

# Runge Kutta 4th Order
def rk4(f, r, t):
    while r[1] > 0:
        x_points.append(r[0])
        z_points.append(r[1])
        k1 = h * f(r, t)
        k2 = h * f(r + k1/2, t + h/2)
        k3 = h * f(r + k2/2, t + h/2)
        k4 = h * f(r + k3, t + h)
        r += (k1 + 2*k2 + 2*k3 + k4) / 6
        t += h
    return t

# Converts radients to degrees
def r_to_d(x):
    return x * 180 / m.pi

# Constants
eta, g, t = 0.3, 9.81, 0
h = 10 ** -2

v = 10
MAX_X, MAX_THETA, SPEED = [], [], []
# Varying the speed from 1 to 45 m/s
while v < 70:
    theta = m.pi / 10
    X_HIT, THETA = [], []

    # Varying theta from m.pi/10 to m.pi / 2
    while theta < m.pi / 2:
        vx, vz = v * m.cos(theta), v * m.sin(theta)
        r = np.array([1, 1, vx, vz], float)
        x_points, z_points = [], []

        t_hit = rk4(f, r, t)
        x_hit = x_points[len(x_points)-1]
        X_HIT.append(x_hit)
        THETA.append(theta)

        theta += m.pi / 1000

    max_hit = max(X_HIT)
    # Find the corresponding theta for max_hit
    MAX_THETA.append(r_to_d(THETA[X_HIT.index(max_hit)]))
    MAX_X.append(max_hit)
    SPEED.append(v)

    v += 3

plt.figure(1)
plt.plot(SPEED, MAX_X)
plt.xlabel('Speed (m/s)')
plt.ylabel('Max Distance (m)')
plt.title('Projectile motion with viscous drag')
plt.savefig('Speed vs Distance')

plt.figure(2)
plt.plot(SPEED, MAX_THETA)
plt.xlabel('Speed (m/s)')
plt.ylabel('Max Theta (Degrees)')
plt.title('Projectile motion with viscous drag')
plt.savefig('Speed vs Theta')
