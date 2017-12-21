// Based on http://physics.oregonstate.edu/~landaur/nacphy/ComPhys/PACKETS/packets.c

#include <stdio.h>
#include <math.h>
#include <time.h>

#define xDim 501 // number space pts, must be odd for simpson

FILE *out1, *out2, *out3a, *out3b, *out3c, *out7a, *out7b, *out7c;
FILE *out8, *out10, *out11, *out12, *out13, *out14, *input;

// Prototypes
void potential();
void initialize(void);
void solveSE(void);
void output();
void probability();

// Global variables
double rePsi[xDim][xDim][2], imPsi[xDim][xDim][2], v[xDim][xDim];
double rho[xDim][xDim], j[xDim][xDim];
double rho1[xDim], rho2[xDim], sumRho[xDim], corr[xDim];
double w[3];
double a1, a2, a3, a4, alpha, dx, dt, er, ei, eri, eii;
double k1, k2, m1, m2, dm1, dm2, dm12, dm22, dxx2, dtx, con, con2;
double ptot, ptotI;
double sol, sig, vmax, x01, x02, y;
int choice, nt, n1, n2, nprint;
time_t timei, timef;

int main() {
    int i, j;
    time_t timeF;
    time_t timeI = time(NULL);
    
    // Inititialzation of variables
    input = fopen("in.dat", "r");
    
}
