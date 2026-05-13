// 9. Faça um algoritmo e o programa em C que leia um número indeterminado 
// de linhas contendo cada um a idade de um indivíduo. O último valor, que não 
// entrará nos cálculos, contém o valor da idade igual a zero. Calcule e mostre a 
// idade média deste grupo de indivíduos.

#include <stdio.h>

int main() {
    int quant;
    printf("Quantas pessoas tem no grupo: ");
    scanf("%d", &quant);
    int vet[quant], tam;
    float med;
    printf("\n\nDigite as idades do grupo(para finalizar digite \"0\")\n");
    for(tam = 0; vet[tam - 1] != 0 && tam <= (quant - 1); tam++) {
        scanf("%d", &vet[tam]);
        if(vet[tam] != 0) {
            med += vet[tam];
        } 
    }
    printf("%d", vet[tam - 1]);
    if(vet[tam - 1] == 0) {
        tam --;
    }
    med = med / tam;
    printf("A media da idade dos alunos eh: %.2f\n", med);

    return 0;
}