#include <stdio.h>
int main() {
    float soma = 0, media, num = 0;
    int quantidade;
    printf("Digite números: \n");
    for(quantidade = 0; num >= 0; quantidade++) {
        scanf("%f", &num);
        if(num >= 0) {
            soma += num;
        }
    }
    quantidade--;
    media = soma/quantidade;
    printf("Soma: %.2f, Média: %.2f, Quantidade de números: %d\n", soma, media, quantidade);
    return 0;
}