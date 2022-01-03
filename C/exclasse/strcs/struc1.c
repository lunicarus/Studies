#include <stdio.h>
#include <string.h>
#include <stdlib.h>
struct cliente //tentei fazer 'cliente[2]' (ter 2 clientes com nome, numero, endereço), mas deu pau
{
char nome[2][10];
char endereco[2][10];
int numero[2][10];
}cliente; //https://www.embarcados.com.br/vetor-de-struct/ (ensina umas coisas, tentei e nd funciona)
int main ( ){
    //cliente pessoas[2]; tentei fazer desse jeito tbm, mas da pau tbm, ele pede ;
    int x;
    for (x = 0;x < 2;x++){
        fflush(stdin);
        printf("digite nome:");
        scanf("%s",cliente.nome[x]);
        fflush(stdin);
        printf("digite endereco:");
        scanf("%s",cliente.endereco[x]);
        fflush(stdin);
        printf("digite numero:");
        scanf("%f",cliente.numero[x]);
    }
        /*nada funciona apartir daqui, tentei com %s,%c no scanf.
        tentei com %s,%c no printf mas ou n imprime, ou imprime alguma insanidade
        */
    for (x = 0;x < 2;x++){ 
    printf("\n%s" "\n%s" "\n%f", cliente.nome[x],cliente.endereco[x],cliente.numero[x]);
    }
}