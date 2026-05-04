// Encontrar o dobro de um número caso ele seja positivo e o seu triplo caso seja 
// negativo, imprimindo o resultado.

#include<stdio.h>

int main() {
    int num1 = 0, result;
    printf("Digite um numero: ");
    scanf("%d", &num1);

    if(num1 > 0) {
        result = num1 * 2;
    } else if(num1 < 0) {
        result = num1 * 3; 
    }
    if(num1 == 0) {
        printf("O o valor digitado é 0\n");
    } else {
        printf("Resultado: %d\n", result);
    }
    return 0;
}