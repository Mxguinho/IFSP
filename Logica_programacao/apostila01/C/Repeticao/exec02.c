/*
2. Preparar um Programa em C que imprima a soma dos quadrados dos 10 
primeiros números inteiros.
*/

#include <stdio.h>
#include <math.h>
int main() {
    int resultado = 0;
    float teste;
    for(int i = 1; i < 10; i++) {
        resultado += i * i;
        printf("%d² + ", i); 
    }
    resultado += 10 * 10;
    printf("10² "); 
    printf("= %d\n", resultado);
    return 0;
}
