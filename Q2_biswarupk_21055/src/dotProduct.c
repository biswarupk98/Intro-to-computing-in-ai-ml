#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include <vectOps.h>

/**
 * @brief Routine to calculate dot product of two vectors
 *
 * @param vect1 Pointer to first vector
 * @param vect2 Pointer to second vector
 * @param vect_len Length of two vectors
 * @param dotpvect Dot proudct of two
 */
double dotProduct(double *vect1, double *vect2, long vect_len)
{
    int i;
    double dotpvect = 0;
    double t_start, t_end;
    t_start = omp_get_wtime();
    
    #pragma omp parallel for default(shared) reduction(+:dotpvect)
    for (i = 0; i < vect_len; i++)
        dotpvect += vect1[i] * vect2[i];

    t_end = omp_get_wtime();

//    printf("Sum of array elements = %lf. Time required to execute = %f seconds\n", dotpvect, t_end - t_start);
    return dotpvect;
}
