#escrita

aluno = input("Digite o nome do aluno: ")
nota1 = input("Digite a primeira nota do aluno: ")
nota2 = input("Digite a segunda nota do aluno: ")
with open("Linguagem_Programacao/aula16/nota.txt", "w") as a:
    a.write(f"{aluno}\n")
    a.write(f"{nota1}\n")
    a.write(f"{nota2}\n")

#leitura
dados = []
with open("Linguagem_Programacao/aula16/nota.txt", "r") as n:
    for i in n:
        dados.append(i)
media = (float(dados[1]) + float(dados[2])) / 2
print(f"A média do aluno {dados[0]} é {media}")