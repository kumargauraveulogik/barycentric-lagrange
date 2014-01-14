#include"lagrange.hpp"
#include<omp.h>

// Constructor
Lagrange::Lagrange(int numInterpPts, double* xInterp, int numEvalPts, double* xEval)
{
    // Loop indices
    int j,k;

    // For storing displacements between interpolation points
    double d;

    ni = numInterpPts;
    ne = numEvalPts;
    xi = xInterp;
    xe = xEval;
  
    // Array of Barycentric weights
    w = new double[ni];

    // Barycentric polynomial ell(x) on evaluation points
    ell = new double[ne]; 

    /* Compute the weights using as slightly modified version of the 
       algorithm on page 504 in the Trefethen & Berrut paper */
    
    w[0] = 1;
    
    // I think this loop can not be parallelized
    for(j=1;j<ni;++j)
    {
        w[j] = 1;

        for(k=0;k<j;++k)
        {
            d = xi[k]-xi[j];
            w[k] *= d;
            w[j] *= -d;
        }
    }

    #pragma omp parallel for
    for(j=0;j<ni;++j)
    {
        w[j] = 1/w[j];
    }
  
    double* ones = new double[ni];     // Create vector of ones
  
    #pragma omp parallel for
    for(j=0;j<ni;++j)
    {
        ones[j] = 1;
    }

    this->bi_sum(ones,ell);    // Compute the ell(x) polynomial

    #pragma omp parallel for
    for(j=0;j<ne;++j)
    {
        ell[j] = 1/ell[j];
    }
 
    delete ones;   
}


Lagrange::~Lagrange()
{
    delete w,ell;
 }

int Lagrange::bi_sum(double* f, double* y)
{
    /* This routine evaluates sums of the form shown in equation (4.2) in 
       the paper by J-P Berrut and L.N. Trefethen */

    // Loop indices
    int j,k;

    #pragma omp parallel for
    for(j=0;j<ne;++j)
    {
        y[j] = 0;
        for(k=0;k<ni;++k)
        {
            if(xe[j] == xi[k])
            {
                y[j] = f[j];
                break;
            }
            else
            {
                y[j] += w[k]*f[k]/(xe[j]-xi[k]);
            }
        }    
    }    
    return 1;
}


int Lagrange::interp(int mi, double* func, int mo, double* poly)
{
    int j;

    this->bi_sum(func,poly);

    #pragma omp parallel for
    for(j=0;j<ne;++j)
    {
        poly[j] *= ell[j];
    }    
    return 1;
}

int Lagrange::get_ne()
{
    return ne;
}




