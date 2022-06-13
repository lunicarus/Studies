	/*Nome dos Integrantes:
		- Lays Lopes Pereira
		- Lucas da Silva Cruz
		- Lucas Moreira Sturchio
		- Rafael de Souza Lima
		- Thais de Jesus Silva Rocha */
#include <iostream>


void Exercicio9(){
    float Vetor[10],menor,maior;

    for(int i = 0;i<10;i++){
        printf("digite a posicao [%d] do vetor: ",i);
        scanf_s("%f",&Vetor[i]);
        if (i == 0){
            menor = Vetor[i];
            maior = Vetor[i];
        }
        if (menor > Vetor[i]){
            menor = Vetor[i];
        }
        if(maior < Vetor[i]){
            maior = Vetor[i];
        }
    }
    printf("Maior: %.4f \nMenor: %.4f",maior,menor);
}
void Exercicio10(){
    float Valores[10],media = 0;
    for(int i = 0;i<10;i++){
            printf("digite o valor [%d] dos 10 valores: ",i+1);
            scanf_s("%f",&Valores[i]);
            media += Valores[i];
        }
    media = media/10;
    printf("media: %f\n",media);
    printf("Valores acima da media:");
    for (int i = 0; i < 10; i++)
    {
        float repeticao;
        if(Valores[i] == repeticao){
            continue;
        }
        else if(Valores[i] > media){
            printf(" %.2f,",Valores[i]);
            repeticao = Valores[i];
        }
    }
    
}


int main(){
    //remover dos comentarios para testagem
    //Exercicio9();
    //Exercicio10();
}