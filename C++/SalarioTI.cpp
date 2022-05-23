#include <stdlib.h>
#include<stdio.h>
#include <math.h>

void mensagem() {

	printf("informe teu cargo, digite 1 para assistente de TI e 2 para Analista de TI: ");

}

int main() {
	int t,c;
	float assistente = 2000;
	float analista = 5000;
	float vales = 800;
	printf("informe o seu turno: digite 1 para matutino, 2 para vespertino e 3 para noturno: ");
	scanf("%d", &t);
	switch (t)
	{
	
	case 1:
		//matutino
		mensagem();
		scanf("%d", &c);
		if (c == 1) //Assistente de TI matutino
		{
			assistente = (assistente * 1.10 + 100 ) - assistente * 0.05; //3100 OK
			printf("o salario do assistente de TI matutino eh de: %f\n", assistente);
			printf("o vale alimentacao eh de 700\n");
			printf("o vale transporte eh de 200\n");

		}
		if (c == 2) { // analista de TI matutino
			analista = (analista * 1.10 + 100 ) - analista * 0.10; // 5800 + 500 - 500 + 100 = 5900 OK
			printf("o salario do analista noturno eh de %f \n", analista);
			printf("o vale alimentacao eh de 700\n");
			printf("o vale transporte eh de 200\n");
		}
		break;
	case 2: //vespertino
		mensagem();
		scanf("%d", &c);
		if (c == 1){ //Assistente de TI vespertino
			assistente = (assistente * 1.20 + 100 ) - assistente * 0.05; // 3200 ok
			printf("o salario do assistente de TI vespertino eh de %f\n", assistente); 
			printf("o vale alimentacao eh de 700\n");
			printf("o vale transporte eh de 300\n");
		}
		if (c == 2) { // analista de TI vespertino
			analista = (analista * 1.20 + 100 ) - analista * 0.10; // 5800 + 1000 = 6800 + 100 = 6900 - 500 = 6400 OK
			printf("o salario do analista noturno eh de %f\n", analista);
			printf("o vale alimentacao eh de 700\n");
			printf("o vale transporte eh de 300\n");
		}
		break;
	case 3: // noturno
		mensagem();
		scanf("%d", &c);
		if (c == 1) //Assistente de TI noturno
		{
			assistente = ((assistente * 1.25 + 100 + 200 ) - assistente * 0.05); // 2500 + 1100 = 3600 - 100 = 3500 OK
			printf("o salario do assistente de TI noturno eh de: %f\n", assistente);
			printf("o vale alimentacao eh de: 800\n");
			printf("o vale transporte eh de 300\n");
		}
		if (c == 2) { // analista de TI noturno
			analista = ((analista * 1.25 + 100 + 200) - analista * 0.10); // 6250 + 1100 = 7350 - 500 = 6850 OK
			printf("o salario do analista noturno eh de: %f\n", analista);
			printf("o vale alimentacao eh de: 800\n");
			printf("o vale transporte eh de: 300\n");
		}
		break;
	default:
		printf("valor de Turno invalido!");
		break;
	}
	return 0;
}