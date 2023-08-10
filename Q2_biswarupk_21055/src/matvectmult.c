#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include <vectHandling.h>
#include <vectOps.h>

void MatVectMult(double *matrix, double *vect, long height, long width, char *filename)
{
    double *output = make1dvect(height);
    int i;
//    printf("###%f", (matrix + 1)[0]);
    double t_start,t_end;
    t_start=omp_get_wtime();
    #pragma omp parallel private(i)
    {   
        int t_id, num_t, start, end, row_partition;
        t_id=omp_get_thread_num();
        num_t=omp_get_num_threads();

        row_partition = height / num_t;
        start = t_id * row_partition;
        end = (t_id + 1) * row_partition;

        for (i = start; i < end; i++)
            output[i] = dotProduct(matrix + i * width, vect, width);

        #pragma omp master
        {
            for (i = row_partition * num_t; i < height; i++)
                output[i] = dotProduct(matrix + i * width, vect, width);
        }

    }
    t_end=omp_get_wtime();
    printf("Matrix multiplication with vector completed in = %f seconds\n", t_end - t_start);
    print1dvect(output, height, filename);
}
