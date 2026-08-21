vendas = [1500, 2000, 800, 3500, 1200]
total = 0
for venda in vendas:
    total += venda

print('soma das vendas da semana:', total)

print('media:', (total / len(vendas)))
maior = vendas[0]
menor = vendas[0]
for venda in vendas:
    if maior < venda:
        maior = venda
    if menor > venda:
        menor = venda
print('maior', maior, '\nmenor', menor)