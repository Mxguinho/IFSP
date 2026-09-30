import funcoes as f

texto = input("Digita um texto: ")

print(f"caracteres: {f.caracteres(texto)}")
print(f"caracteres: {f.caracteres2(texto)}")
print(f"texto invertido: {f.inverter(texto)}")
print(f"vogais sem acento: {f.vogais(texto)}")
print(f"vogais: {f.vogais2(texto)}")

num = int(input("Digita um numero maior que 2: "))

print(f"Fibonacci: {f.fibonacci(num)}")

