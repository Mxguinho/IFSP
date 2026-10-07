alunos = ["laise", "heitor", "vasco", "Carlos", "fabricia"]
with open("Linguagem_Programacao/aula16/alunos.txt", "w") as a:
    a.write(f"Lista de alunos Reprovados:\n")
    for aluno in alunos:
        a.write(f"Aluno(a): {aluno}\n")
    a.writelines(alunos)