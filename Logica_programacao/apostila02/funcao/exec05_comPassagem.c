// Faça uma função que recebe a idade de uma pessoa em anos, meses e 
// dias e retorna essa idade expressa em dias.

#include <stdio.h>

void calcularIdadeEmDias(int anos, int meses, int dias) {
    int totalDias;
    totalDias = (anos * 365) + (meses * 30) + dias;
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

    calcularIdadeEmDias(anos, meses, dias);

    return 0;
}