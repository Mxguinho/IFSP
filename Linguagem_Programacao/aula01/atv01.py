altura = float(input("Digite a altura do cilindro: "))
raio = float(input("Digite o raio do cilindro: "))

lateral = 2 * 3.14 * raio * altura
base = 3.14 * (raio ** 2)
area = base + lateral
litros = area / 3
latas = litros / 5
custo = latas * 50

print("Área do cilindro: ", area)
print("Litros necessários: ", litros)
print("Latas necessárias: ", latas)
print("Custo total: ", custo)

