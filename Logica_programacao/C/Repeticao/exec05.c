/*
5. Faça um programa que imprima na tela todos os números pares de um 
intervalo informado pelo usuário.
*/

#include <stdio.h>

int main() {
    int num1, num2;
    printf("Digite um numero: ");
    scanf("%d", &num1);
    printf("Digite um numero: ");
    scanf("%d", &num2);
    
    if(num1 < num2){
        for(int i = num1 ; i <= num2; i++) {
            if((i % 2) == 0) {
                printf("%d\t", i);
            }
        }
    } else if(num1 == num2){
        printf("Os numeros são iguais!!!");
        if((num1 % 2) == 0) {
            printf("\nO numero é par!!!");
        } else {
            printf("\nO numero é impar!!!");
        }
    } else if(num1 > num2) {
        for(int i = num2 ; i <= num1; i++) {
            if((i % 2) == 0) {
                printf("%d\t", i);
            }
        }
    }
    printf("\n");
}