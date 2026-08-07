#b) Ler uma temperatura em graus Fahrenheit e apresentá-la convertida em graus Celsius. A fórmula de conversão é C ((F-32)5)/9, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.

F = int(input("Digite a temperatura em graus Fahrenheit: "))

C = ((F - 32) * 5) / 9

print("Sua temperatura em Graus Fahrenheit: Celsius", C)