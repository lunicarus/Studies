#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void formula(float x1, float x2){
    float P,S;
    
    S = x1+x2;

    P = x1*x2;
    printf("x² - %.2fx + %.2f\n", S,P);
}
void raizes(float a, float b, float c){
    //x² - 12x + 32
    float x1,x2;
    x1 = (-b + ( sqrt(pow(b,2)-(4*a*c)) ) ) /(2*a); //-b + sqrt(b² - 4ac)/2a
    x2 = (-b - ( sqrt(pow(b,2)-(4*a*c)  ) ) ) /(2*a);
    printf("%f\n%f\n",x1,x2);
}
int main(){
    formula(4,8);
    raizes(1,-12,32);
}