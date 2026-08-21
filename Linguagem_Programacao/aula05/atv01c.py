# c) Construir um programa que apresente a soma dos cem primeiros números naturais (1+2+3+...+98 + 99+100).


result = 0
for i in range (1, 101):
    result += i
print("resultado:", result)