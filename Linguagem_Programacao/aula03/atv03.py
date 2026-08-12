# e) Efetuar a leitura de três valores numéricos (representados pelas variáveis A, B e C) e processar o cálculo da equação completa de segundo grau, utilizando a fórmula de Bhaskara (considerar para a solução do problema todas as possíveis condições para delta: delta < 0 não há solução real, delta > 0- há duas soluções reais e diferentes e delta = 0 há apenas uma solução real). Lembre-se de que é completa a equação de segundo grau que possui todos os coeficientes A, B e C diferentes de zero. O programa deve apresentar respostas para todas as condições estabelecidas para delta.
while(True):
    A = int(input("Digite o valor de A: "))
    if(A == 0):
        print("A não pode ser zero")
        break
    B = int(input("Digite o valor de B: "))
    C = int(input("Digite o valor de C: "))

    delta = B**2 -4*A*C

    if(delta < 0):
        print(f"Não há solução real {delta}")
    elif(delta == 0):
        print(f"Há uma solução real possível {delta}")
    else:
        print(f"Há duas soluções reais possíveis {delta}")

    # resultado = (-B +- (delta // 2)) / 2 * A