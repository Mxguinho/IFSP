numeros = [1, 2, 3, 4, 5]

quadrado = []

for x in numeros:
    quadrado.append(x ** 2)
print(quadrado)

quadrado = [x ** 2 for x in numeros]
print(quadrado)