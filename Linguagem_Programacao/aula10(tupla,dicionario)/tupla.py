#tupla é imutavel

tupla = (10,20,30,40,50)
descontos = (10,15,20)

corolla = (2025, "chumbo")

#coordenadas

ifsp_catanduva = (-21.14713, -48.94542)

#conexão de banco de dados

connection = ("localhost", "8080", "database_lipa.db")

#acessar

print(tupla[0])
print(tupla[0:2])

# tupla[2] = 8 #da erro
# print(tupla[2])

x, y, z = descontos
print(x)
print(y)
print(z)

n = (5, )

print(type(n))

#percorrrer uma tupla
for item in descontos:
    print(item)