/*
3. Faça um programa onde o usuário digita um valor, e imprima na tela todos 
os valores entre 0 e o valor digitado.
*/
#include <stdio.h>

int main() {
    int num1;
    printf("Digite um valor: ");
    scanf("%d", &num1);

    if(num1 < 0){
        for(int i = num1; i <= 0; i++) {
            printf("%d\t", i);
        }
    } else if(num1 == 0){
        printf("O valor digitado eh 0!!!");
    } else if(num1 > 0) {
        for(int i = 0; i <= num1; i++) {
            printf("%d\t", i);
        }
    }
    printf("\n");

    return 0;
}