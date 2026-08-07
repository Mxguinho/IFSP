# g) Ler quatro valores numéricos inteiros e apresentar os resultados armazenados em memória das adições e multiplicações utilizando o mesmo raciocínio aplicado quando do uso de propriedades distributivas para a máxima combinação possível entre as quatro variáveis. Não é para calcular a propriedade distributiva, deve-se apenas usar a sua forma de combinação. Considerando a leitura de valores para as variáveis A, B, C e D, devem ser feitas seis adições e seis multiplicações, ou seja, deve ser combinada a variável A com a variável B, a variável A com a variável C, a variável A com a variável D. Depois, é necessário combinar a variável B com a variável C e a variável B com a variável D e, por fim, a variável C será combinada com a variável D.

A = int(input("Digite o valor da variável A: "))
B = int(input("Digite o valor da variável B: "))
C = int(input("Digite o valor da variável C: "))
D = int(input("Digite o valor da variável D: "))

soma_AB = A + B
soma_AC = A + C
soma_AD = A + D
soma_BC = B + C
soma_BD = B + D
soma_CD = C + D

mult_AB = A * B
mult_AC = A * C
mult_AD = A * D
mult_BC = B * C
mult_BD = B * D
mult_CD = C * D

print("Resultados das adições:")
print("A + B =", soma_AB)
print("A + C =", soma_AC)
print("A + D =", soma_AD)
print("B + C =", soma_BC)
print("B + D =", soma_BD)
print("C + D =", soma_CD)

print("Resultados das multiplicações:")
print("A * B =", mult_AB)
print("A * C =", mult_AC)
print("A * D =", mult_AD)
print("B * C =", mult_BC)
print("B * D =", mult_BD)
print("C * D =", mult_CD)