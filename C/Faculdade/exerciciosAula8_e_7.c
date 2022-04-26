#include <stdio.h>
#include <stdlib.h>
#include <iostream>

//função da media ponderada de notas
void media(float a, float b, float c, float d){
    float ponderada;
    ponderada = ((a*2)+(b*2)+(c*3)+(d*3))/10;
        if (a > 10 || b > 10 || c > 10){
        printf("nota invalida!\n");
        ponderada = 100000;
    }
    if (ponderada >= 9 && ponderada <= 10){
        printf("A\n");
    }
    else if (ponderada >= 7.5 && ponderada < 9){
        printf("B\n");
    }
    else if (ponderada >= 6 && ponderada < 7.5){
        printf("C\n");
    }
    else if (ponderada >= 4 && ponderada < 6){
        printf("D\n");
    }
    else if (ponderada < 4){
        printf("E\n");
    }
    else{
        printf("Error\n");
    }

}
//Pega o valor de 'sexo' e imprime se é valido ou não.
void masculinoFeminino() {
	char sexo;
	printf("digite M para masculino e F para feminino");
	scanf_s("%c", &sexo);
	if (sexo == 'M') {
		printf("Masculino");
	}
	else if (sexo == 'F') {
		printf("Feminino");
	}
	else {
		printf("valor de 'Sexo' invalido!");
	}

}

void impares() {
	for (int i = 1;i < 30; i++) {
		if (i % 3 == 0) {
			cout << i << endl;
		}
		else {
			continue;
		}
	}
}

//Realiza ajustes de salario
float salario(float sal){
    if (sal < 500){
        return sal = sal*1.15;
    }
    if (sal >= 500 && sal < 1000){
        return sal *= 1.10;
    }
    if (sal > 1000){
        return sal *= 1.05;
    }
    return sal == 0;
}
//Outro exercicio de reajuste de salario
float aumentoDiferente(float salario) {
	if (salario <= 0) {
		printf("Valor de salario invalido! valor nulo entregue: ");
		return NULL;
	}
	if (salario <= 1000) {
		printf("o seu salario reajustado é de: ");
		return salario *= 1.25;
	}
	else {
		printf("o seu salario é de: ");
		return salario *= 1.15;
	}
}

//realiza operações de soma até o usuario digitar 0
void soma (){
    float i=0,r=-1,aux;
    while (r != 0){
        if (i == 0){
            printf("informe um valor para soma\n");
            scanf("%f", &r);  
            printf("%f + 0 = %f\n",r,r); 
            i += r;
        }
        else {
            printf("informe um valor para soma\n");
            scanf("%f", &r);
            aux = i;
            i += r;
            printf("%f + %f = %f\n",aux,r,i);
        }   
    }
}
//imprime o fatorial de um numero
int fatoral(int a){
    int b,aux;
    b = a;
    aux = b;
    for(int i = 1;i < aux;i++){
        b -= 1;
       a = b*a; 
    }
    return a;
}

//faz a sequencia fibonacci
void fibonacii(){
    int a=0,b=1,total=0;
    printf("1 ");
    for(int i = 0; i < 10; i++){
        total = a+b;
        printf(" %d ", total);
        a = b; 
        b = total;
    }

}
int main(){
    fibonacii();
    return 0;
}
