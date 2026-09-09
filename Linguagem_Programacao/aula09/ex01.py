lista = []
media = 0

for i in range(4):
    lista.append(int(input("Digite uma nota: ")))
    media += lista[i]

media = media / len(lista)

if(media < 4):
    print(f"{media}: reprovado")
elif(media < 6):
    print(f"{media}: aprovado")
else:
    print(f"{media}: milagre")

