# d) Ler os valores de quatro notas escolares bimestrais de um aluno representadas pelas variáveis N1, N2, N3 e N4. Calcular a média aritmética (variável MD1) desse aluno e apresentar a mensagem "Aprovado" se a média obtida for maior ou igual a 7; caso contrário, o programa deve solicitar a quinta nota (nota de exame, representada pela variável NE) do aluno e calcular uma nova média aritmética (variável MD2) entre a nota de exame e a primeira média aritmética. Se o valor da nova média for maior ou igual a cinco, apresentar a mensagem "Aprovado em exame"; caso contrário, apresentar a mensagem "Reprovado". Informar também, após a apresentação das mensagens, o valor da média obtida pelo aluno.

N1 = int(input("Digite sua primeira nota: "))
N2 = int(input("Digite sua segunda nota: "))
N3 = int(input("Digite sua terceira nota: "))
N4 = int(input("Digite sua quarta nota: "))

medA = (N1 + N2 + N3 + N4) / 4

if(medA >= 7):
    print(f"Aprovado, nota: {medA}")
else:
    print(f"Reprovado")
    N5 = int(input("Digite sua quinta nota(recuperação): "))
    medA2 = (medA + N5)/2
    if(medA2 >= 5):
        print(f"Aprovado em exame, nota: {medA2}")
    else:
        print(f"Reprovado, nota: {medA2}")


