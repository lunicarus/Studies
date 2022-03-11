#include <stdio.h>
#include <stdlib.h>
#include <math.h>
 //! Resolver problema de atribuição no array(multiplicação esta incorreta!)
 //todo Uso de pow(lista[i],3) resolveria, porem o mesmo n funciona direito no VSCode
void SquareArray(double list[],int d){
    int i,x = 0, n = 3;
                while (x < d){
                    for(i=0;i < n;i++){
                        list[i] = list[i]*list[i];
                        x++;
                    }
                }
}
int main(){
    double lista[] = {2,3,4};
    SquareArray(lista,4);
    int i;
    for (i = 0; i < 3; i++){
        printf("\n %f \n",lista[i]);
    }
}