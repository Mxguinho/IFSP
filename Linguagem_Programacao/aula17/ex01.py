import csv
pessoas = [
    ['nome', 'idade', 'cidade'],
    ['layzy', 28, 'novo horizonte'],
    ['marcus', 56, 'São Paulo']
]

with open("Linguagem_Programacao/aula17/pessoas.csv", "w", newline = "", encoding = "UTF-8" ) as arquivo:
    registro = csv.writer(arquivo)
    registro.writerows(pessoas)
print('O arquivo foi criado com sucesso')