#include <stdio.h>
int main() {
    int n[3], central;
    for(int i = 0; i < 3; i++) {
        printf("\nDigite um número: ");
        scanf("%d", &n[i]);
    }
    int min = n[0];
    if (n[1] < min) min = n[1];
    if (n[2] < min) min = n[2];

    int max = n[0];
    if (n[1] > max) max = n[1];
    if (n[2] > max) max = n[2];

    int meio = n[0] + n[1] + n[2] - min - max;

    printf("\nNúmero central: %d\n", meio);
    
    return 0;
}