// Faça um algoritmo que leia dois valores inteiros A e B se os valores forem iguais deverá 
// se somar os dois, caso contrário multiplique A por B. Ao final de qualquer um dos 
// cálculos deve-se atribuir o resultado para uma variável C e mostrar seu conteúdo na 
// tela. 

#include <stdio.h>

int main () {
    int A, B, C;
    char continuar;


    printf("Digite 2 valores(se iguais serao somados, se diferentes serao multiplicados): \n");
    scanf("%d", &A);
    scanf("%d", &B);

    if (A == B) {
        C = A + B;
        printf("O resultado da soma eh: %d\n", C);
    } else {
        C = A * B;
        printf("O resultado da multiplicacao eh: %d\n", C);
    }
}