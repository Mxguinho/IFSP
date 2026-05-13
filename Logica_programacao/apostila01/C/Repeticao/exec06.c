/*
6. Um funcionário de uma empresa recebe aumento salarial anualmente. 
Sabe-se que:
 a) Esse funcionário foi contratado em 2015, com salário inicial de R$ 
1000,00;
 b) Em 2016 recebeu aumento de 1,0% sobre seu salário inicial;
 c) A partir de 2016, os aumentos corresponderam ao dobro do percentual 
anterior.
Faça um algoritmo e o programa em C que determine o salário atual desse 
funcionário.
*/

#include <stdio.h>
#include <time.h>

int main() {
    time_t data_ano;
    time(&data_ano);
    struct tm *data = localtime(&data_ano);
    
    int anoAtual = (data->tm_year) + 1900;
    float salInitial = 1000, salAtual = 0;
    
    printf("O ano atual é: %d\n\n", anoAtual);
    printf("Ano   |  Salario\n-----------------\n");

    for(int i = 2015; i <= anoAtual; i++) {
        if(i == 2015) {
            salAtual = salInitial;
        } else if(i == 2016) {
            salAtual += (salAtual * 0.01);
        } else if(i > 2016) {
            salAtual += (salAtual * 0.02);
        }
        printf("%d  |  %.2f\n", i, salAtual);    
    }
    printf("\n");
    return 0;
}