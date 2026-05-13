#include <stdio.h>
#include <stdlib.h>
int main() {
int i, soma = 0;
for (i=1; i <= 10; i++) {
soma = soma + i;
}
printf("A soma dos números entre 1 e 10 é %d", soma);
return 0;
}