#include <stdlib.h>
#include <stdio.h>

double pow(double val,double ex){
    double tt = val;
    for(int i=1;i < ex;i++){
        val = val*tt;
    }
    return val;
}
int main(){
    double total,numero,exponencial;
    printf("informe um numero e um exponencial:\n");
    scanf("%lf %lf",&numero,&exponencial);
    total = pow(numero,exponencial);
    printf("\n%.2f\n",total);
}