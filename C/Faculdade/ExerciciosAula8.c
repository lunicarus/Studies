#include <stdlib.h>
#include <math.h>
#include <stdio.h>
//*concluido
// "pega a media de 5 alunos e da a media da classe"
void avg(int list[])
{
    for (int i = 0; i < 5; i++)
    {
        printf("informa a nota do aluno %d:", i + 1);
        scanf("%d", &list[i]);
    }
    double total = 0, average;
    for (int i = 0; i < 5; i++)
    {
        total += list[i];
    }
    average = total / 5;
    printf("%.2f\n", average);
}
//* Concluido
// "le 5 valores numericos inteiros de uma matriz e imprime a soma dos pares"
void sum(int list[])
{
    for (int i = 0; i < 5; i++)
    {
        printf("informa valores inteiros da matriz %d:", i + 1);
        scanf("%d", &list[i]);
    }

    int soma = 0;
    for (int i = 0; i < 5; i++)
    {
        if (list[i] % 2 == 0)
        {
        soma += list[i];
        }
    }
    printf("a soma dos numeros pares é:%d\n",soma);
}
//* Concluido
// "ordena matriz com 5 elementos de forma crescente OU decrecente"
void ordenar(int list[]){
    printf("programa que ordena elementos 5 elementos\n");
    for (int i = 0; i < 5; i++)
    {
        printf("informe valor %d:", i + 1);
        scanf("%d", &list[i]);
    }
    printf("Digite 0 para ordem crescente e 1 para decrescente.\n");
    int caso;
    scanf("%d", &caso);
    switch (caso)
    {
    case 0:
        int aux;
        for(int i = 0; i < 4;i++){

            for(int j = 0; j<4;j++){

            if(list[j] > list[j+1]){
                aux = list[j];
                list[j] = list[j+1];
                list[j+1] = aux;
            }   

            }
            

        }
        break;
    
    case 1:
        aux = 0;
        for(int i = 0; i < 4;i++){

            for(int j = 0; j < 4;j++){

            if(list[j] < list[j+1]){
                aux = list[j];
                list[j] = list[j+1];
                list[j+1] = aux;
            }   

            }
            

        }
        break;
    default:
        printf("Opção invalida!");
        break;
    }
int listaOD;
for(int i = 0; i < 5;i++){
            listaOD = list[i];
            printf("%d, ", listaOD);
        }
}

//! Falta este exercicio a ser feito
void cadastro(){

}
/* "Desenvolver um programa que simule uma agenda de cadastro pessoal com nome, endereço, bairro e telefone de 10 pessoas. 
Ao final, o programa deve apresentar seus elementos dispostos em ordem crescente (na variável NOME)."
*/

int main()
{
    int matriz[5];
    // avg(matriz);
    // sum(matriz);
    // ordenar(matriz);
}