area_total = 0

while True:
	nome_comodo = input("Digite o nome do cômodo: ")
	largura = float(input("Digite a largura do cômodo, em metros: "))
	comprimento = float(input("Digite o comprimento do cômodo, em metros: "))

	area_comodo = largura * comprimento
	area_total += area_comodo

	print(f"A área do(a) {nome_comodo} é {area_comodo:.2f} m².")

	continuar = input("Deseja calcular outro cômodo? (S/N): ").strip().lower()

	if continuar in ("n", "nao", "não"):
		break

print(f"A área total da residência é {area_total:.2f} m².")

