ex01 = 'Instituto'
ex02 = 'Federal'
ex03 = '''
Instituto Federal de São Paulo 
Campus Catanduva
Curso ADS
'''

print(ex01[2])

print(len(ex03))

for item in ex01:
    print(item)

for i in range(len(ex01)):
    print(i, ex01[i])

print(ex01[1:8:2])

# formatando string

reajuste = 10
inflacao = 6.5

frase = 'reajuste: %d%%; inflação: %.2f%%' % (reajuste, inflacao)

print(frase)

print('Instituto \\ Federal')
print(R'Instituto \\ Federal')
print('Instituto %d%% Federal' % (10))
print(u'Instituto %% Federal')

comando = ex01 + " " + ex02
print(comando)

al01 = "Josefina"
al02 = "Felisberto"
al03 = "josefina"

#tabela ASCII

if(al01 == al03):
    print("iguais")
else:
    print("diferentes")

if(al01 < al02):
    print(f"{al01} vem antes do {al02}")
else:
    print(f"{al02} vem antes do {al01}")

if(al01 in al03):
    print(f"{al01} esta dentro de {al03}")
else:
    print(f"{al01} não esta em {al03}")

print(al03.upper())
print(al03.lower())
print(ex03.strip())#tira os espaços do começo e do fim
print(ex03.replace(" ", "-"))#substitui

print(ex03.split())#separa
ex03_elementos = ex03.split()

for elementos in ex03_elementos:
    print(elementos)

print(ex03.split("e")) #cria a lista atravez do caracter