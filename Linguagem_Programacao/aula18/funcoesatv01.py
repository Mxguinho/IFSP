import csv

def coletardados():
    notas = [['nome', 'nota01', 'nota02']]
    for i in range(5):
        nome = input("Digite o nome do aluno: ")
        nota01 = float(input("Digite a primeira nota do aluno: "))
        nota02 = float(input("Digite a segunda nota do aluno: "))
        notas.append([nome, nota01, nota02])
    return notas

def criar_arquivo(notas):
    with open("Linguagem_Programacao/aula18/notas.csv", "w", encoding = "utf-8") as arquivo:
        registro = csv.writer(arquivo)
        registro.writerows(notas)

def fazer_media():
    with open("Linguagem_Programacao/aula18/notas.csv", "r", encoding = "utf-8") as arquivo:
        registro = csv.DictReader(arquivo)
        medias = []
        for linha in registro:
            media = ((float(linha["nota01"]) + float(linha["nota02"])) / 2)
            if (media < 4):
                status = "reprovado"
            elif (media >= 4 and media <= 6):
                status = "recuperação"
            elif (media > 6):
                status = "aprovado"

            medias.append({
                "nome": linha["nome"],
                "media": media,
                "status": status
            })

        return medias