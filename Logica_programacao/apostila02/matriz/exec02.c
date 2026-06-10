//2.  Faça um programa que carregue uma matriz 3x4 com números 
//inteiros, calcule e mostre a quantidade de elementos entre 15 e 20.

#include <stdio.h>

void PrintMatriz(int linha, int coluna, float matriz[linha][coluna]) {
    for(int i = 0; i < linha; i++) {
        for (int j = 0; j < coluna; j++) {
            printf("%.2f ", matriz[i][j]);
        }
        printf("\n");
    }
}

int main() {
    int linha = 3, coluna = 4;
    float matriz[linha][coluna], elementos = 0;

    printf("Digite valores para completar uma matriz %dx%d:\n", linha, coluna);

    for(int i = 0; i < linha; i++) {
        printf("Digite a %dª linha:\n", i + 1);
        for (int j = 0; j < coluna; j++) {
            scanf("%f", &matriz[i][j]);
            if(matriz[i][j] >= 15 && matriz[i][j] <= 20) {
                elementos++;
            }
        }
        
    }
    printf("Soma dos valores ente 15 e 20(considerando 15 e 20): %.2f\n", elementos);

    PrintMatriz(linha, coluna, matriz);
    return 0;
}