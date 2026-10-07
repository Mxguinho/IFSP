import csv
with open("Linguagem_Programacao/aula17/pessoas.csv", "r", encoding = "utf-8") as arquivo:
    registro = csv.DictReader(arquivo)

    for linha in registro:
        print(linha["nome"], linha["idade"], linha["cidade"])