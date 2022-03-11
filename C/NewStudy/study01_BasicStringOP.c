#include <stdlib.h>
#include <stdio.h>
void flush_in()
{
    int ch;
    while ((ch = fgetc(stdin)) != EOF && ch != '\n')
    {
    } //elimina os b.o do scanf
}
int main(){
    char name[20]; // string type array
    char nameM[20]; // string type array
    char nameL[20]; // string type array
    int Age; //Integer type
    printf("define your age and name");
    scanf("%d",&Age);
    flush_in();
    scanf("%s%s%s",name,nameM,nameL);
    printf( "my name is %s %s %s and i'm %d\n", name,nameM,nameL,Age);
return 0;
}
