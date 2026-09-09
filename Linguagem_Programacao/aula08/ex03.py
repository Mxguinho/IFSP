lista_anilhada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for lista in lista_anilhada:
    for item in lista:
        print(item)
print('\n')

for y in range(len(lista_anilhada)):
    for x in range(len(lista_anilhada[y])):
        print(f"{y}x{x}", lista_anilhada[y][x])
    