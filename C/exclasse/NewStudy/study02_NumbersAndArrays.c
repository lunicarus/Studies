#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void SquareArray(double list[]){
    int i;
    for (i = 0; i < 3; i++){
        list[i] = pow(list[i],2);
    }
}
int main(){
    double lista[] = {2,3,4};
    SquareArray(lista);
    int i;
    for (i = 0; i < 3; i++){
        printf("\n %f \n",lista[i]);
    }
}