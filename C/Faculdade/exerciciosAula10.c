#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// strlcpy (Char variable,"stringValue",char variable size);

//Converte data tipo ("DD/MM/YYYY") para ("Dia DD de M de YYYY")
int ConverteDATA()
{
    //*Finished, works as intended
    char data[20];

    printf("informe a data Do formato DD/MM/YYYY que deseja converter: ");
    scanf("%s", data);
    char *subpartes;

    subpartes = strtok(data, "/");
    int dia = atoi(subpartes);
    if (dia < 1 || dia > 31)
    {
        printf("Dia invalido!");
        return 0;
    }
        
    subpartes = strtok(NULL, "/");

    int mes = atoi(subpartes);
    subpartes = strtok(NULL, "/");
    if (mes < 1 || mes > 12)
        {
            printf("Mes Invalido!");
            return 0;
        }
        
    int ano = atoi(subpartes);
    subpartes = strtok(NULL, "/");
    if (ano < 1900)
        {
        printf("Ano invalido!");
        return 0;
        }
    printf("Dia %d de ", dia);
    switch (mes){
        case 1:
            printf(" Janeiro de");
            break;

        case 2:
            printf(" Fevereiro de");
            break;

        case 3:
            printf(" Março de");
            break;

        case 4:
            printf(" Abril de");
            break;

        case 5:
            printf(" Maio de");
            break;

        case 6:
            printf(" Junho de");
            break;

        case 7:
            printf(" Julho de");
            break;

        case 8:
            printf(" Agosto de");
            break;

        case 9:
            printf(" Setembro de");
            break;

        case 10:
            printf(" Outubro de");
            break;

        case 11:
            printf(" Novembro de");
            break;

        case 12:
            printf(" Dezembro de");
            break;

        default:
            printf("Mes invalido!");
            break;
    }
    printf(" %d\n", ano);
        return 0;
}

int main()
{
    //ConverteDATA();
    for(int i = 1;i<100; i+= i++){
        printf("%d ",i);
    }
}