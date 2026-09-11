#dicionario armazena coleções utilizando o conceito chave-valor

aluno = {"nome":"frederico", "nota":3.5}
print(aluno)
print(aluno["nome"])
print(aluno["nota"])

aluno["nota"] = 5
print(aluno["nota"])

#adicionar chave

aluno["disciplina"] = "LIP"
print(aluno["disciplina"])

banco_de_dados = {
    'cli_001':{'nome':'alice','idade':25,'cidade':'São Paulo'},
    'cli_002':{'nome':'bob','idade':30,'cidade':'Rio de Janeiro'},
    'cli_003':{'nome':'carol','idade':28,'cidade':'Belo Horizonte'}
}
print(banco_de_dados)
print(banco_de_dados['cli_001']['nome'])

banco_de_dados['cli_001']['idade'] = 95

for chave in banco_de_dados['cli_001']:
    print(f"{chave}: {banco_de_dados['cli_001'][chave]}")

for valor in banco_de_dados['cli_001'].values():
    print(valor)

for c, v in banco_de_dados['cli_001'].items():
    print(f"{c}: {v}")

