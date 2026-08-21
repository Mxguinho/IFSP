lista = [10, 20, 30, 40, 50]

print(lista[0])

lista[0] = int(input('digite um valor: '))
lista[1] = lista[0] + lista[2]

if (lista[1] > 5):
    print('valor =', lista[1])
print('tamanho:', len(lista))
print(lista[-5]) # Pega o tamanho da lista e subtrai 5 para apresentar o valot