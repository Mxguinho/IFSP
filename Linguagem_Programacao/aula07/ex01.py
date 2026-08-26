import copy  # Importa o módulo que possui a função deepcopy().

lista = [1, 2, 3, 4, 5]  # Cria uma lista com cinco números inteiros.

print(lista[2:4])  # Exibe os itens dos índices 2 até antes do índice 4.

print(lista[2:])  # Exibe os itens do índice 2 até o final da lista.

print(lista[:3])  # Exibe os itens do início até antes do índice 3.

print(lista[:])  # Cria e exibe uma cópia superficial com todos os itens.

print(lista[0:5:2])  # Exibe os itens dos índices 0 a 4, pulando de 2 em 2.

print(2 * lista)  # Repete os itens da lista duas vezes em uma nova lista.

lista_copia = lista  # Atribui a mesma lista; não cria uma nova lista.
print(id(lista))  # Exibe o identificador do objeto original na memória.
print(id(lista_copia))  # Exibe o mesmo identificador, pois ambas apontam para o mesmo objeto.
lista[0] = 100  # Altera o primeiro item da lista original.
print(lista)  # Exibe a lista depois da alteração.
print(lista_copia)  # Também exibe a alteração, pois é uma referência ao mesmo objeto.

lista_copia2 = lista.copy()  # Cria uma cópia superficial, com outro objeto de lista.
print(id(lista))  # Exibe o identificador da lista original.
print(id(lista_copia2))  # Exibe outro identificador, pois a lista foi copiada.
lista[3] = 2  # Altera somente a lista original.
lista_copia2[0] = 4  # Altera somente a cópia superficial neste exemplo.
print(lista)  # Exibe a lista original, sem a alteração feita na cópia.
print(lista_copia2)  # Exibe a cópia, sem a alteração feita na lista original.

lista_copia3 = copy.deepcopy(lista)  # Cria uma cópia profunda, copiando também objetos aninhados.
print(id(lista))  # Exibe o identificador da lista original.
print(id(lista_copia3))  # Exibe outro identificador, pois é um novo objeto.
lista[3] = 3  # Altera somente a lista original.
lista_copia3[0] = 2  # Altera somente a cópia profunda.
print(lista)  # Exibe a lista original, independente da cópia profunda.
print(lista_copia3)  # Exibe a cópia profunda, independente da lista original.
