#include <stdio.h>

int main() {
    float area, tinta, latas ,preco;
    printf("Digite a area a ser pintada: ");
    scanf("%f", &area);
    tinta = area / 3;
    latas = tinta / 18;
    preco = latas * 80;
    printf("Area: %.2f, Litros: %.2f, Latas: %.2f, Preço: %.2f\n", area, tinta, latas, preco);
    return 0;
}