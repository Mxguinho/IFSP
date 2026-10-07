import csv
#coloca o cabeçalho
with open("Linguagem_Programacao/aula17/pessoas2.csv", "r", encoding = "utf-8") as arquivo:
    registro = csv.DictReader(arquivo, fieldnames = ['Nome', 'Idade', 'Cidade'])
    for linha in registro:
        print(linha["Nome"], linha["Idade"], linha["Cidade"])