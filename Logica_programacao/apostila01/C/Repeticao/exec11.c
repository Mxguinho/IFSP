// 11. Faça   um   algoritmo   e   o   programa   em   C   que   leia   uma   quantidade 
// indeterminada de números positivos e conte quantos deles estão nos seguintes 
// intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada dos dados deverá 
// terminar quando for lido um número negativo.

#include <stdio.h>
#ifdef _WIN32
    #include <windows.h>   // Para Sleep no Windows
#else
    #include <unistd.h>    // Para sleep/usleep no Linux/macOS
#endif

// Função de delay em milissegundos
void delay_ms(unsigned int milliseconds) {
    if (milliseconds == 0) return; // Evita chamadas desnecessárias

#ifdef _WIN32
    Sleep(milliseconds); // Windows: milissegundos
#else
    // Linux/macOS: usleep usa microssegundos
    usleep(milliseconds * 1000);
#endif
}

int main() {
    int ate25 = 0, de26_50 = 0, de51_75 = 0, de76_100 = 0, quant, tam, num;
    
    printf("Digite numeros de 0 a 100(numeros negativos ou maiores que 100 finalizam)\n");
    for(tam = 0; num >= 0 ; tam++) {
        scanf("%d", &num);
        if(num <= 100) {
            if(num >= 0 && num <= 25) {
            ate25++;
            } else if(num >= 26 && num <= 50) {
                de26_50++;
            } else if(num >= 51 && num <= 75) {
                de51_75++;
            } else if(num >= 76 && num <= 100) {
                de76_100++;
            } else {
                printf("Encerrando!!!\n\n");
                delay_ms(1200);
        }}
    }
    printf("de 0 a 25: %d\nde 26 a 50: %d\nde 51 a 75: %d\nde 76 a 100: %d\n", ate25, de26_50, de51_75, de76_100);
    printf("Total: %d\n", (tam - 1));
    return 0;
}