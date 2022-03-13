#include <stdlib.h>
#include <stdio.h>
#include <math.h>

int main(){
    int i,j;
    double total,exponencial = 3;
    double numero[2][5] = {
        {2,3,6,9,10} , 
        {4,7,12,15,11}
    };
    for(i = 0; i<2;i++){
        printf("\n");
        for(j = 0; j < 5;j++){
            total = pow(numero[i][j],exponencial);
            printf("%.2lf  ", total);
        }
    }
    printf("\n");
    return 0;
}