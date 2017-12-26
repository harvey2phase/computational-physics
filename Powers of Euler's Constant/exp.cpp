#include<iostream>
#include<cmath>

#define ACCURACY std::pow(10.0, -7)

// Prototypes
double myexp(double);
double powSeries(double, double, double);



int main() {
    for (int i = 0; i < 20; i++)
        std::cout << myexp(i) << "\n";
    return 0;
}

// Evaluates e^x using the power seires
// The function returns when the next item in the power series is less than ACCURACY (i.e. the improvment in accruacy is negligible)
double myexp(double x) {
    double N = 1;
    double fact = 1;
    double sum = powSeries(x, N, fact) + 1;

    N++;
    fact *= N;
    double nextSeries = powSeries(x, N, fact);

    while (nextSeries > ACCURACY && N < 30) {
        sum += nextSeries;
        N++;
        fact *= N;
        nextSeries = powSeries(x, N, fact);
    }
    return sum;
}

// Returns the value of the Nth item in the power seires
double powSeries(double x, double N, double fact) {
    return (std::pow(x, N) / fact);
}
