lista = []
lista_nomes = []

alunos = 2 #int(input("quantos alunos: "))

for i in range(alunos):
    lista_nomes.append(str(input("digite seu nome: ")))
    lista.append(int(input("Digite sua nota: ")))

for i in range(alunos):
    print(f"{lista_nomes[i]} {lista[i]}")
    if(lista[i] < 4):
        print("reprovado")
    elif(lista[i] < 6):
        print("aprovado")
    else:
        print("milagre")

print(lista_nomes)
print(lista)