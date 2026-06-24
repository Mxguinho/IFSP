// Escreva uma função que recebes 3 valores reais X, Y e Z e que verifique se esses valores podem ser 
// os comprimentos dos lados de um triângulo e, neste caso, retornar qual o tipo de triângulo formado. 
// Para que X, Y e Z formem um triângulo é necessário que a seguinte propriedade seja satisfeita: o 
// comprimento de cada lado de um triângulo é menor do que a soma do comprimento dos outros dois 
// lados. A função deve identificar o tipo de triângulo formado observando as seguintes definições:
// Triângulo Equilátero: os comprimentos dos 3 lados são iguais.
// Triângulo Isósceles: os comprimentos de 2 lados são iguais.
// Triângulo Escaleno: os comprimentos dos 3 lados são diferentes.

#include <stdio.h>

void tipo_triangulo(float x, float y, float z) {
    if (x < y + z && y < x + z && z < x + y) {
        if (x == y && y == z) {
            printf("Triângulo Equilátero\n");
        } else if (x == y || x == z || y == z) {
            printf("Triângulo Isósceles\n");
        } else {
            printf("Triângulo Escaleno\n");
        }
    } else {
        printf("Não é um triângulo\n");
    }
}

int main() {
    float x, y, z;

    printf("Digite o comprimento do lado X: ");
    scanf("%f", &x);
    printf("Digite o comprimento do lado Y: ");
    scanf("%f", &y);
    printf("Digite o comprimento do lado Z: ");
    scanf("%f", &z);

    tipo_triangulo(x, y, z);
    return 0;
}