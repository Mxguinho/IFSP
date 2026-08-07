#C) Calcular e apresentar o valor do volume de uma lata de óleo, utilizando a fórmula VOLUME 3.14159*R+2* ALTURA.

altura = float(input("Digite a altura da lata: "))
raio = float(input("Digite o raio da lata: "))

VOLUME = (3.14 * (raio ** 2)) * altura

print("Volume da lata: ", VOLUME)   