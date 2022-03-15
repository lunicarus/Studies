#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void flush_in()
{
    int ch;
    while ((ch = fgetc(stdin)) != EOF && ch != '\n')
    {
    } //elimina os b.o do scanf
}
void LavarCarro()
{
    printf("Lavagem de Carro Concluida! \n\n");
}
    /*void ConsultaFilaL()
{
   printf("filaPrincipal de Lavagem: \n\n");
    for(int x  = 0; x < CarrosN1; x++){
        printf("%s",Fila1[x]);    
    }
    return 0; 
}*/
void ConsultaFilaE()
{
    printf("filaPrincipal de filaEspera: \n\n");
}
void Encerrar()
{
    printf("programa encerrado!\n\n");
}
struct TCarro{                   //devine A estrutura tipo TCarro com as variaveis Placa,Modelo e dono.
    char placa[10]; //[] devine a quantidade maxima de caracteres presentes na variavel
    char modelo[10];
    char dono[20];
};//declara uma variavel matrix do tipo TCarro.
    struct TCarro AddCarro(){
    struct TCarro carro;
    flush_in();
    printf("Informe o nome do Dono!\n");
    fgets(carro.dono, 20, stdin);
    printf("Informe o nome do placa!\n");
    fgets(carro.placa, 20, stdin);
    printf("Informe o nome do Modelo!\n");
    fgets(carro.modelo, 20, stdin);
    return carro;//cria as subrotinas que depois serão chamadas no codigo
}
int main(void){
    struct TCarro carro;
    int CarrosN, menu, contEspera = 0, contPrincipal = 0, i = 0;
    struct TCarro *filaPrincipal,filaEspera[3];
    printf("Sistema de lavagem de carros, por favor, informe o numero de carros: ");
    scanf("%d", &CarrosN);
    filaPrincipal = (int *) malloc(CarrosN * sizeof(int));
    system("cls");
    printf("voce tera no maximo %d Carros na lavagem e %d Carros no total\n", CarrosN, CarrosN + 3);
    while (menu != 5)
    {
        printf("\n1-Adicionar carro na fila\n2-Lavar carro (lava o primeiro)\n3-Consultar fila de lavagem\n4-Consultar fila de espera\n5-Encerrar\n");
        printf("...........................................................................................\n");
        scanf("%d", &menu); //usei varios \n pra ficar apresentavel.
        switch (menu)
        {
        case 1:
            if (CarrosN > contPrincipal) // 1 > 1 //verificar se há espaço na fila principal
            {
                printf("Adicionando um carro na fila principal\n");
                filaPrincipal[contPrincipal] = AddCarro();
                contPrincipal++;
                break;
            }
            else if ( CarrosN >= contPrincipal && contEspera < 3) // 1 > 1 //verificar se há espaço na fila espera e testar se principal esta cheia
            {
                filaEspera[contEspera] = AddCarro();
                contEspera++;
                printf("carro adicionado na fila de espera!\n");
                break;
            }
            else{
                printf("Capacidade Maxima atingida!\n"); 
                break;
            }

        case 2:
            if(contPrincipal == 0 && contEspera == 0){
                printf("Fila vazia!");
                break;
            }
            if (contPrincipal > 0 && contEspera == 0){// 1 > 1 //verificar se há espaço na fila espera e testar se principal esta cheia
            printf("Primeiro carro da fila foi lavado!\n");
            // [0] = [1] // [1] = [2]
               for(i = 1; i < contPrincipal; i++){
                    filaPrincipal[i-1] = filaPrincipal[i];
            }
            contPrincipal--;
            break;
            }
            if(contPrincipal > 0 && contEspera > 0){
            printf("Primeiro caro lavado, adicionado primeiro da espera na parte vazia!\n");
                for(i = 1; i < contPrincipal; i++){ //[]
                    filaPrincipal[i-1] = filaPrincipal[i];
            }
                contPrincipal--;
                filaPrincipal[contPrincipal] = filaEspera[0];
                for(i = 1; i < contEspera; i++){
                    filaEspera[i-1] = filaEspera[i]; 
            }
                
                contEspera--;
                break;
            }
            //imprime posição 0 sera lavada
            //mover o visinho para esquerda
            //verificar se existe carro na fila de espera
            //contPrincipal sempre vazia(no topo) //filaPrincipal[contPrincipal] = filaReserva[0]
            LavarCarro();
            break;

        case 3:
                printf("Fila Principal!\n");
                printf("%d", contPrincipal);
                for(i = 0; i <= contPrincipal; i++){
                 printf("posição %d\n: dono:%s\nplaca:%s\nmodelo:%s",i, filaPrincipal[i].dono,filaPrincipal[i].placa,filaPrincipal[i].modelo);
            }
            //ConsultaFilaL(&filaPrincipal,CarrosN);
            break;

        case 4:
            //ConsultaFilaE();
                printf("Fila De  espera!\n");
                printf("%d", contEspera);
                for(i = 0; i <= contEspera; i++){
                printf("posição %d\n: dono:%s\nplaca:%s\nmodelo:%s",i, filaEspera[i].dono,filaEspera[i].placa,filaEspera[i].modelo);
            }
            break;
        case 5:
            Encerrar();
            break;

        default:
            printf("Opção invalida!\n");
            break;
        }
    }
    return 0;
}