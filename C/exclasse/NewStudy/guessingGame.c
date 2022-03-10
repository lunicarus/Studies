#include <stdlib.h>
#include <stdio.h>
#include <time.h>

//! Retornar ao codigo futuramente para finalizar o jogo
//! Problemas com verificação de igualdade entre os elementos das matrizes

int  main(){
    srand(time(NULL));
    int rs = rand() % 2;
    switch(rs != 5){
                char resposta[20];
                char capital1[20] = "Brasilia";
                char capital2[20] = "Tokyo";
        case 0:
            printf("Qual é a capital do Brasil?\n");
            scanf("%s", resposta);
            printf("%s",resposta);
            if(resposta == capital1){
                printf("Resposta Correta!\n");
                break;
            }
            else{
                printf("Resposta Incorreta!");
                int rs = rand() % 2;
        }
        case 1:
            printf("Qual é a capital do Japão?\n");
            scanf("%s", resposta);
            if(resposta == capital2){
                printf("Resposta Correta!");
                break;
            }
            else{
                printf("Resposta Incorreta!");
                int rs = rand() % 2;
        }
    }
    return 0;
}

//? função que testa geração de valores aleatorios via rand()
int randNum(){
    srand(time(NULL)); //semente aleatoria gerada apartir do tempo atual
        int n = 5;
        int i;
        for(i = 0; i < n; i++){
            printf("%d ", rand() % 2); //imprime valor aleatorio
        }
}