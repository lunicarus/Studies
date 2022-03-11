#include <stdlib.h>
#include <stdio.h>

struct student{
    char ID[50];
    char nome[100];
    char curso[50];
    double CoeficienteA;
};

int main(){
    struct student lucas;
    strcpy(lucas.curso,"Analise e desenvolvimento de sistemas");
    strcpy(lucas.nome,"Lucas da Silva Cruz");
    strcpy(lucas.ID,"B2A25K");
    lucas.CoeficienteA = 0.56;

    printf(lucas.nome);
 }