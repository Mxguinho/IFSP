import csv
with open("Linguagem_Programacao/aula17/pessoas.csv", "r", encoding = "utf-8") as arquivo:
    registro = csv.reader(arquivo)

    for linha in registro:
        print(linha)