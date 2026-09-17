nome = input("Digite seu nome: ")

print("maiusculo:", nome.upper())
print("minusculo:", nome.lower())
print("quantidade de caracteres:", len(nome))

print("quantidade de caracteres(desconsiderando espaços):", len(nome.replace(" ", "")))
