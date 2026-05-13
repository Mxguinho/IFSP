// Faça um programa onde o usuário digita dois valores, e imprima na tela 
// todos os valores no intervalo entre os valores digitados.

#include <stdio.h>
int main() {
    int num1, num2;

    printf("Digite um valor: ");
    scanf("%d", &num1);
    printf("Digite outro valor: ");
    scanf("%d", &num2);

    if(num1 < num2){
        for(int i = 0; (num1 + i) <= num2; i++) {
            printf("%d\t", (num1 + i));
        }
    } else if(num1 == num2){
        printf("Os numeros são iguais!!!");
    } else if(num1 > num2) {
        for(int i = 0; (num1 - i) >= num2; i++) {
            printf("%d\t", (num1 - i));
        }
    }
    printf("\n");
    
    return 0;
}