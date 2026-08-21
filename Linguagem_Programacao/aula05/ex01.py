n = 5
notas = []
media = 0
print("Digite a nota dos alunos")

for i in range (n):
    x = float(input(f"nota do aluno {i + 1}: "))

    notas.append(x)
    media += x
media = media / n

aluno = 0
for x in notas:
    aluno += 1
    if x > media:
        if x > media:
            print(f"aluno {aluno} Aprovado:", x)