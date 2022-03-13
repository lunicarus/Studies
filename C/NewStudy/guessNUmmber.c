#include <stdio.h>
#include <stdlib.h>

int main(){

    int Nguess = 0, trueGuess = 5,userGuess;
    while (userGuess != trueGuess && Nguess < 3){
        printf("Try to guess the lucky number (0-10):");
        scanf("%d",&userGuess);
        Nguess++;
    }
    (userGuess == trueGuess) ? printf("You win!\n") : printf("You lose\n");

}