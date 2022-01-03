#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void bubble(int list[], int n){
//@ Ordenates the String 
int c, d, t;
 
for (c = 0 ; c < ( n - 1 ); c++){
  for (d = 0 ; d < n - c - 1; d++){
    if (list[d] > list[d+1]){         
      t         = list[d];
      list[d]   = list[d+1];
      list[d+1] = t;
      }
    }
  }
}
void flush_in(){

int ch;
while ((ch = fgetc(stdin)) != EOF && ch != '\n')
{
}
}
void inicializaVetor(int *vetor, int n){   
flush_in();
int i;
int valor;
for (i = 0; i < n; i++){
  scanf("%d", &valor);
  vetor[i] = valor;
  }
}
int soma(int *vetor, int n,int *total){   
  int i;
  for ( i = 0; i < n; i++){
    *total+= vetor[i];
  }
}
void imprimeVetor(int *vetor, int n){  
    int i;
    for (i = 0; i < n; i++)
    {
        printf("%d\n",vetor[i]);
    }
}
void maiorMenor(int *vetor, int n, int *maior, int *menor){ 

    *menor = vetor[0];
    *maior = vetor[n-1]; 
}
int main(void){
    int tamanho = 0,total = 0,Maior = 0,*vetor,Menor = 0,*m,*M;
    M = &Maior;
    m = &Menor;
scanf("%d", &tamanho);
if(tamanho > 0){
     vetor = (int *) malloc(tamanho * sizeof(int));
    inicializaVetor(vetor, tamanho);
    bubble(vetor, tamanho);
    maiorMenor(vetor,tamanho,M,m);
    soma(vetor, tamanho,&total);
    imprimeVetor(vetor, tamanho);
    printf("Maior:[%d] Menor:[%d] Soma[%d]",Maior,Menor,total);

}
else{
    printf("Não foi possível alocar!");
}
return 0;
}