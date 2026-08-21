lista = [1, 2, 3, 4, 5, 6, 7, 8]
print(lista)
soma = 0
for i in range(len(lista)):
    lista[i] = int(input('digite: '))
    soma += lista[i]
    

print('lista:',lista)

print('tamanho:', len(lista))
''
print('media:', soma / len(lista))
print('elementos | potencia')
for i in range(len(lista)):
    print('       ', i, '|', lista[i] ** 2)
print('elementos | raiz')
for i in range(len(lista)):
    print('       ', i, '|', lista[i] ** 0.5)