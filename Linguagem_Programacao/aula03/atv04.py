# g) Fazer a leitura de quatro valores numéricos inteiros representados pelas variáveis A, B, C e D. Apresentar apenas os valores que sejam divisíveis por 2 e 3.

A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))
D = int(input("Digite o valor de D: "))

div = 0

if(A % 2 == 0 and A % 3 == 0):
    print(f"O valor de A é divisível por 2 e 3: {A}")
    div+=1
if(B % 2 == 0 and B % 3 == 0):
    print(f"O valor de B é divisível por 2 e 3: {B}")
    div+=1
if(C % 2 == 0 and C % 3 == 0):
    print(f"O valor de C é divisível por 2 e 3: {C}")
    div+=1
if(D % 2 == 0 and D % 3 == 0):
    print(f"O valor de D é divisível por 2 e 3: {D}")
    div+=1
if(div == 0):
    print(f"Nenhum deles é divisivel por 2 e 3")
print(f"A: {A}\nB: {B}\nC: {C}\nD: {D}")