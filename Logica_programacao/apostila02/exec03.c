// Escreva um programa C que utilize um vetor para armazenar a idade de 
// um conjunto de N indivíduos, número este fornecido pelo usuário. 
// Calcule a média de idade deste grupo de indivíduos, 
// e determine o número de pessoas que tiveram idade inferior à média.

#include <stdio.h>

int main() {
    int tam, soma, menorMedia; 
    float med;

    printf("Quantos individuos tem no grupo?\n");
    scanf("%d", &tam);

    int idades[tam];

    printf("Digite a idade de cada individuo em sequencia: \n");
    for(int i = 0; i < tam; i++) {
        scanf("%d", &idades[i]);
        soma += idades[i];
    }
    med = soma / tam;

    for(int i = 0; i < tam; i++) {
        if(idades[i] < med) {
            menorMedia++;
        }
    }
    printf("Individuos: %d  Media: %.1f  Individuos abaixo da media: %d\n", tam, med, menorMedia);

    return 0;
}