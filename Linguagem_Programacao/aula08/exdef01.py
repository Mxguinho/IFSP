def soma(a, b):
	soma = a + b
	return soma
def vezes(a, b):
	mult = a * b
	return mult
def divisao(a, b):
	if(b == 0):
		return 'impossivel dividir por 0'
	div = a / b
	return div

print('soma:', divisao(int(input('digite um numero inteiro: ')), int(input('digite um numero inteiro: '))))