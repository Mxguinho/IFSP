// 4. Crie uma função em linguagem C que receba 3 números e retorne o 
// menor valor. 

#include <stdio.h>

float fuc() {
    float num1, num2, num3;
    printf("Digite o número 1\n");
    scanf("%f", &num1);
    printf("Digite o número 2\n");
    scanf("%f", &num2);
    printf("Digite o número 3\n");
    scanf("%f", &num3);

    float maior = num1;
    if (maior <  num2)
    {
        maior = num2;
    }

    if (maior <  num3)
    {
        maior = num3;
    }

    return maior;
}

int main() {
    
    float maior = fuc();
    printf("Maior numero: %.2f\n", maior);
    return 0;
}