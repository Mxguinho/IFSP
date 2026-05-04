/*
7. Faça um algoritmo e o programa em C que receba o salário de um 
funcionário X. Sabe-se que o funcionário Y tem um salário equivalente a 1/3 do 
salário de X. X aplicará seu salário integralmente na caderneta de poupança, 
rendendo 2% ao mês e Y aplicará seu salário integralmente no fundo de renda 
fixa, que está rendendo 5% ao mês. Calcule e mostre a quantidade de meses 
necessários para que o valor pertencente a Y iguale ou ultrapasse o valor 
pertencente a X.
*/

#include <stdio.h>
int main() {
    float salX, salY;
    printf("Digite seu salário: ");
    scanf("%.2f", &salX);

    salY = salX / 3;

    //continuar
    return 0;
}