#include <stdio.h>
int main ( ){   
	float media;
	printf("informe a média: ");

	scanf("%f", &media);
    (media >= 7) ? printf("aprovado") : (media>=4) ? printf("final") : printf("reprovado");
return 0;
}
