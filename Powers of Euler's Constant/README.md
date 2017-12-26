## Powers Of Euler's Constant

### Overview

This project explores methods to evaluate e^x without using existing math functions or precomputed values of e.

`exp.cpp` utilizes a simple Dynamic Programming technique to improve the time complexity while `exp.py` takes a more brute-force approach.

### Details

`exp.py`  defines the function `myexp()` which evaluates the value of e^x using the infinite power series e = &sum; <sup>1</sup>&frasl;<sub>n!</sub> as n goes from 0 to infinity.

Accuracy is the difference the result of the power series up until N-1 and that of N. The program stops when increasing N no longer changes the result of the evaluated e, i.e. when the difference is less than accuracy.

`exp.cpp` takes the same approach but improves on it with simple a Dynamic Programming technique. Instead of re-evaluating the summation of the series and n! every time n is increased, both values for n-1 are stored and readily available for the computation of n, and therefore saving time.

### Testing

`exp` is the executable (object code) built from `exp.cpp`. Simply download the programs and run them. Both C++ and Python programs print out the value of e^x from x = 0 to x = 19.
