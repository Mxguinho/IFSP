import csv
nome = input("Digite o nome do aluno: ")
idade = int(input("Digite a idade do aluno: "))
cidade = input("Digite a cidade do aluno: ")

with open("Linguagem_Programacao/aula17/pessoas2.csv", "a", newline = "", encoding = "utf-8") as arquivo:
    registro = csv.writer(arquivo)
    registro.writerow([nome, idade, cidade])
print("nota do aluno registrada com sucesso")

print("\n")
with open("Linguagem_Programacao/aula17/pessoas2.csv", "r", encoding = "utf-8") as arquivo:
    registro = csv.DictReader(arquivo, fieldnames = ['Nome', 'Idade', 'Cidade'])
    for linha in registro:
        print(linha["Nome"], linha["Idade"], linha["Cidade"])