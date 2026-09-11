tupla = (1,2,3,4,5,6,7,8,9,10)
pares = []
for item in tupla:
    if(item % 2 == 0):
        pares.append(item)

print(tupla)
print(pares)

alunos = {
'aluno1' : {"nome":"jesriberto", "idade":98, "curso":"ADS"},
'aluno2' : {"nome":"joao", "idade":75, "curso":"nenhum"},
'aluno3' : {"nome":"everton", "idade":30, "curso":"agropecuaria"}
}

for lunos in alunos:
    for info in alunos[lunos]:
        print(f"{info}: {alunos[lunos][info]}")