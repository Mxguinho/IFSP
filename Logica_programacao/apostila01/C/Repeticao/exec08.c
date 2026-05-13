// 8. Supondo que a população de um país A seja da ordem de 90.000.000 de 
// habitantes com uma taxa anual de crescimento de 3% e que a população de um 
// país B, seja aproximadamente de 200.000.000 de habitantes com uma taxa 
// anual de crescimento de 1,5%, fazer um algoritmo e o programa em C que 
// calcule e escreva o número de anos necessários para que a população do país A 
// ultrapasse   ou   se   iguale   a   população   do   país   B,   mantidas   estas   taxas   de 
// crescimento.

#include <stdio.h>

int main() {
    int anos = 0, habit_A = 90000000,  habit_B = 200000000;
    float acres_A = 1.03, acres_B = 1.015;
    printf("Cidade A: %d\tCidade B: %d\tAnos: %d\n\nQuantos anos para os habitantes da cidade A alcanças os da cidade B?\n\n", habit_A, habit_B, anos);
    while(habit_A < habit_B) {
        anos++;
        habit_A = habit_A * acres_A;
        habit_B = habit_B * acres_B;
    } 
    printf("Cidade A: %d\tCidade B: %d\tAnos: %d\n", habit_A, habit_B, anos);
    return 0;
}