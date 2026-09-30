def soma(num1, num2):
    return num1 + num2 
def subtracao(num1, num2):
    return num1 - num2 
def multiplicacao(num1, num2):
    return num1 * num2 
def divisao(num1, num2):
    return num1 / num2 
def IMC(peso, altura):
    imc = peso / ((altura / 100) ** 2)
    return "Abaixo do peso" if imc < 18.5 else "Peso normal" if imc < 24.9 else "Sobrepeso" if imc < 29.9 else "Obeso" if imc < 34.9 else "IMC inválido"
def fatorial(num):
    for i in range(num + 1):
        resultado = 1
        resultado *= (i + 1)
    return resultado