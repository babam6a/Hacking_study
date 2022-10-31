#include <stdio.h>
#include <math.h>

int main(){
    char buffer[10];
    scanf("%s",buffer);
    if (isdigit(buffer[2]))
        printf("True\n");
}   
