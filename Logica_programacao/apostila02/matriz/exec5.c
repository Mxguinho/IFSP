// 5.  Dada uma matriz de ordem 3x3 faça um programa que faça a leitura 
// de um inteiro qualquer. Calcule o produto desse elemento por todos os 
// elementos da matriz, colocando o resultado em outra matriz.

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
    int linha = 3, coluna = 3, multiplicador;
    float matriz01[linha][coluna], matriz02[linha][coluna], soma = 0;

    printf("Digite um valor inteiro para multiplicar a matriz: ");
    scanf("%d", &multiplicador);

    printf("\nDigite valores para completar uma matriz %dx%d:\n", linha, coluna);

    for(int i = 0; i < linha; i++) {
        printf("Digite a %dª linha:\n", i + 1);
        for (int j = 0; j < coluna; j++) {
            scanf("%f", &matriz01[i][j]);
            matriz02[i][j] = matriz01[i][j] * multiplicador;
        }
        
    }

    printf("Matriz Escrita por você: \n");
    PrintMatriz(linha, coluna, matriz01);
    printf("\n");
    printf("Matriz criada a partir da multiplicação: \n");
    PrintMatriz(linha, coluna, matriz02);
    return 0;
}