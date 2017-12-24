## Powers Of Euler's Constant

### Purpose

This project evaluates the value of e to the power of x (often denoted as `exp(x)` in many math libraries, including that of Python) using the infinite power series

&sum;<sub>i=0;

h<sub>&theta;</sub>(x) = &theta;<sub>o</sub> x + &theta;<sub>1</sub>x

### Details


Accuracy is the difference the result of the power series up until N-1 and that of N. The program stops when increasing N no longer changes the result of the evaluated e, i.e. when the difference is less than accuracy.
