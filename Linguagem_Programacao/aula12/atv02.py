texto = input("Digite seu texto: ")
letra = input("qual letra quer encontrar: ")[0]
qnt = 0

for char in texto.lower():
    if char.lower() == letra:
        qnt += 1

print(f"Quantidade de {letra}: {qnt}")

palavras = texto.split(" ")
print(palavras)
print(f"Quantidade de palavras: {len(palavras)}")