#include <stdlib.h>
#include <stdio.h>
#include <math.h>

int main(){
    int i;
    double total,exponencial = 3;
    double numero[5] = {2,3,6,9,10};
    for(i = 0; i<5;i++){
        total = pow(numero[i],exponencial);
        printf("%.2lf\n", total);
    }
}