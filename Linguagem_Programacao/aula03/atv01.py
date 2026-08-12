#C) Realizar a leitura dos valores de quatro notas escolares bimestrais de um aluno representadas pelas variáveis N1, N2, N3 e N4. Calcular a média aritmética (variável MD) desse aluno e apresentar a mensagem "Aprovado" se a média obtida for maior ou igual a 5; caso contrário, apresentar a mensagem "Reprovado". Informar também, após a apresentação das mensagens, o valor da média obtida pelo aluno.

N1 = int(input("Digite sua primeira nota: "))
N2 = int(input("Digite sua segunda nota: "))
N3 = int(input("Digite sua terceira nota: "))
N4 = int(input("Digite sua quarta nota: "))

medA = (N1 + N2 + N3 + N4) / 4

if(medA >= 5):
    print(f"Aprovado, nota: {medA}")
else:
    print(f"Reprovado, nota: {medA}")


