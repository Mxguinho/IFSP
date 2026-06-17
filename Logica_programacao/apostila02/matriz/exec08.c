// 8. Escreva uma função que recebe como parâmetros três números inteiros a, 
// b e c, sendo a maior que 1. A função deverá somar todos os inteiros entre 
// b e c que sejam divisíveis por a (inclusive b e c) e retornar o resultado 
// para o programa principal.

#include <stdio.h>

int somaDivisiveis(int a, int b, int c) {
    int soma = 0;

    if(b > c) {
        int temp = b;
        b = c;
        c = temp;
    }
    
    for (int i = b; i <= c; i++) {
        if (i % a == 0) {
            soma += i;
        }
    }
    return soma;
}

int main() {
    int a, b, c;
    printf("Digite o valor de a (maior que 1):\n");
    scanf("%d", &a);
    printf("Digite o valor de b:\n");
    scanf("%d", &b);
    printf("Digite o valor de c:\n");
    scanf("%d", &c);

    if (a <= 1) {
        printf("O valor de a deve ser maior que 1.\n");
        return 1;
    }

    int resultado = somaDivisiveis(a, b, c);
    printf("A soma dos inteiros entre %d e %d que são divisíveis por %d é: %d\n", b, c, a, resultado);
    
    return 0;
}