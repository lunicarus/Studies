#include <iostream>
using namespace std;

int Fibbonaci(int i){
    cout << '1' << endl;
    int num = 0;
    int num2 = 1;
    int aux;
    for(i;i>1;i--){
        cout << (num+num2) << endl;
        aux = num2;
        num2 = num+aux;
        num = aux;


    }
    return 0;
}
int Fatorial(int fatorial){
    int b,aux;
    b = fatorial;
    aux = b;
    for(int i = 1;i < aux;i++){
        b -= 1;
       fatorial = b*fatorial; 
    }
    cout << fatorial << endl;
    return 0;
}