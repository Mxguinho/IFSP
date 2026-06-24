// Faça uma função que recebe, por parâmetro, um valor N e calcula e escreve a tabuada de 1 até N.

#include <stdio.h>

void tabuada(int num1) {

    for(int i = 1; i <= num1; i++) {
        int resultado = num1 * i;
        printf("%d x %d = %d\n", i, num1, resultado);
    }
}

int main() {

    printf("Digite um valor inteiro: ");
    int num1;
    scanf("%d", &num1);

    tabuada(num1);
    return 0;
}