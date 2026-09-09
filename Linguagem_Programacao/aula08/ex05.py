numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = []

for x in numeros:
    if x % 2 == 0:
        pares.append(x)
print(pares)

pares = [x for x in numeros if x % 2 == 0]
print(pares)