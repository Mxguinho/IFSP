import calculadora as c

while(True):

    n1 = int(input("Digite um numero (se 0 finaliza o programa): "))

    if n1 == 0:
        print("Finalizando calculadora...")
        break

    operacao = input("Escolha a operação: +, -, *, /, i(IMC), f(Fatorial): ")[0]

    if(operacao == 'f'):
        print(c.fatorial(n1))
        continue


    n2 = int(input("Escolha outro número: "))

    match operacao:
        case '+':
            print(c.soma(n1, n2))
        case '-':
            print(c.subtracao(n1, n2))
        case '*':
            print(c.multiplicacao(n1, n2))
        case '/':
            print(c.divisao(n1, n2))
        case 'i':
            print(c.IMC(n1, n2))
        case _:
            print("Operação inválida")
            continue




