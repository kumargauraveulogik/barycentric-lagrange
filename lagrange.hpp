// lagrange.hpp

class Lagrange{
    public:
        Lagrange(int,double*, int, double*);
        ~Lagrange();

        // Interpolate from the interpolation to the evaluation points
        int interp(int,double*,int, double*);

        /* Implement sum formulas as found in equation 4.2 of Trefethen 
           and Berrut SIAM Review, Vol. 46, No. 3, pp.501-517 */
        int bi_sum(double* f, double* y);

        // Because I don't know how to determine this at the Cython level
        int get_ne();

    private:
        // Number of interpolation points
        int ni;

        // Number of evaluation points
        int ne;

        // Values of interpolation points  
        double *xi; 

        // Values of evaluation points
        double *xe;

        // Interpolation weights
        double *w;

        // Barycentric multiplicative polynomial
        double *ell;

};
