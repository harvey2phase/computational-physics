## Random Walk

### Overview

This Project simulates a random walk in 2 dimensional space.

### Details

This project contains a single file `random_walk.py`, which does the following things:

* Provides a visual simulation of 1,000 particles undergoing random walks in 2-D.

* Graphs the root mean square (RMS) of the particles' distances from the origin vs. time.

* Graphs the RMS of the particles' maximum distances from the origin vs. time.

* Graphs the ratio of the maximum RMS and RMS of distances (M/R) vs. time.

There are several objects in the visual simulation, each representing a different set of data:

* *The red dots*: represent the particles in 2-D making the random walks.

* *The green dots*: represent the maximum points of each particle when it is furthest away from the origin.

* *The red circle*: represents the root mean square (RMS) of the particles' distances from the origin.

* *The green circle*: represents the RMS of the maximum points' distances.

### Testing

Download the project and run `random_walk.py`.

The default value for `iterations` is 1,000, which represents the number of random steps taken. Changing this variable will change the number of steps taken. One can also can the `for` loop on line 41 to `while true`, running the simulation indefinitely.