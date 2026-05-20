// 4. Escreva um programa C que utilize um vetor para armazenar um conjunto de 
// N elementos inteiros, número este fornecido pelo usuário. 
// Verifique e imprima quantos desses elementos são positivos e quantos são negativos.

#include <stdio.h>

int main() {
    int tam, maior0, menor0; 

    printf("Quantos numeros inteiros deseja inserir?\n");
    scanf("%d", &tam);

    int numeros[tam];

    printf("Digite os numeros em sequencia: \n");
    for(int i = 0; i < tam; i++) {
        scanf("%d", &numeros[i]);
        if(numeros[i] < 0) {
            menor0++;
        } else if(numeros[i] >= 0) {
            maior0++;
        }
    }
    printf("numeros: %d  positivos: %d  negativos: %d\n", tam, maior0, menor0);

    return 0;
}