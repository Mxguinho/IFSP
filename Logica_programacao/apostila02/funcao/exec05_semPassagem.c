// Faça uma função que recebe a idade de uma pessoa em anos, meses e 
// dias e retorna essa idade expressa em dias.

#include <stdio.h>

int totalDias;

void printDias() {
    printf("A idade total em dias é: %d\n", totalDias);
}

int main() {
    int anos, meses, dias;

    printf("Digite a idade em anos: ");
    scanf("%d", &anos);

    printf("Digite a idade em meses: ");
    scanf("%d", &meses);

    printf("Digite a idade em dias: ");
    scanf("%d", &dias);

    totalDias = (anos * 365) + (meses * 30) + dias;

    printDias();

    return 0;
}