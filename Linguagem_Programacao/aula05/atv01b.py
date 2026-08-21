# b) Elaborar um programa que mostre os resultados da tabuada de um número qualquer, a qual deve ser apresentada de acordo com sua forma tradicional.

num = int(input("Digite um numero: "))

for i in range (11):
    print(f"{num} x {i} = {num * i}")
    
    