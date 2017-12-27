# RANDOM WALK
# by Harvey Wang
# Created October 2017

import math as m
import random as ran
import numpy as np
import vpython as vp
import matplotlib.pyplot as plt
import time as t

# Define the constant parameters
iterations = 1000
n = 1000
r = 0.1
s = 0.1

# Setup the canvas
d = vp.canvas(x = 200, y = 200, width = 700, height = 700, center = vp.vector(0, 0, 5), background = vp.color.white)
d.autoscale = False
vp.rate(1000)

# Create an array of 1000 spheres
# Create another array of the same length to mark the maximums
s_array = np.empty(n, vp.sphere)
m_array = np.empty(n, vp.sphere)
for i in range(n):
    s_array[i] = vp.sphere(radius = r, color = vp.color.red)
    m_array[i] = vp.sphere(radius = r, color = vp.color.green)

# Create a black sphere to mark the origin
origin = vp.sphere(radius = 0.15, color = vp.color.black)

# Create rings to represent the RMS of spheres and maxes
sph_rin = vp.ring(axis = vp.vector(0, 0, 1), thickness = 0.1, color = vp.color.red)
max_rin = vp.ring(axis = vp.vector(0, 0, 1), thickness = 0.1, color = vp.color.green)

start = t.time()

# Move the n spheres randomly
for j in range(iterations):
    r_sum = 0
    m_sum = 0

    for i in range(n):
        dx = (2 * ran.random() - 1) * s
        dy = (2 * ran.random() - 1) * s
        s_array[i].pos += vp.vector(dx, dy, 0)

        # Calculate distances and sums from origin
        d_sph = m.sqrt(s_array[i].pos.x ** 2 + s_array[i].pos.y ** 2)
        d_max = m.sqrt(m_array[i].pos.x ** 2 + m_array[i].pos.y ** 2)
        r_sum += d_sph ** 2
        m_sum += d_max ** 2

        # Check for the max point
        if d_sph > d_max:
            m_array[i].pos = s_array[i].pos

    # Calculate and plot the RMS of the spheres and the maximums
    r_RMS = m.sqrt(r_sum / n)
    m_RMS = m.sqrt(m_sum / n)
    sph_rin.radius = r_RMS
    max_rin.radius = m_RMS
    plt.figure(1)
    plt.scatter(t.time() - start, r_RMS)
    plt.figure(2)
    plt.scatter(t.time() - start, m_RMS)
    plt.figure(3)
    plt.scatter(t.time() - start, m_RMS / r_RMS)

# Configure the graphs
plt.figure(1)
plt.ylabel("RMS of the spheres")
plt.title("RMS of the Spheres vs. Time")
plt.xlabel("Time (s)")
plt.figure(2)
plt.ylabel("RMS of the maximums")
plt.title("RMS of the Maximums vs. Time")
plt.xlabel("Time (s)")
plt.figure(3)
plt.title("RMS of Spheres over Maximums vs. Time")
plt.ylabel("RMS of Spheres over Maximums")
plt.xlabel("Time (s)")
plt.show()
