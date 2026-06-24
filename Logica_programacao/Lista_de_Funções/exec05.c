// Faça uma função que receba um valor inteiro e positivo e calcula o seu fatorial.

#include <stdio.h>

void fatorial(int num1) {
    int resultado = num1;

    for(int i = num1 - 1; i > 0; i--) {
        resultado *= i;
    }
    printf("O fatorial de %d = %d\n", num1, resultado);
}

int main() {

    printf("Digite um valor inteiro positivo: ");
    int num1;
    scanf("%d", &num1);

    fatorial(num1);
    return 0;
}