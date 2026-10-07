n = open("Linguagem_Programacao/aula16/nome.txt", "w")
for i in range(1000):
    n.write(f"{i + 1}: Eu te amo\n")
n.close()