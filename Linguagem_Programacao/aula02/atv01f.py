#F) Ler dois vatores para as variáveis A e B e efetuar a troca dos valores de forma que variável A passe o possuir o valor da variável B e a variável B passe a possuir o valor da variável A. Apresenta alores após a efetivação do processamento da troca.

A = int(input("Digite o valor da variável A: "))
B = int(input("Digite o valor da variável B: "))
C = A
A = B
B = C
print("Valores após a troca:")
print("A =", A)
print("B =", B) 