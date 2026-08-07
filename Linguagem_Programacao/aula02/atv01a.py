# a) Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit. A fórmula de conversão é FC*9/5+32, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.

C = int(input("Digite a temperatura em graus celsius: "))

F = ((C * 9) / 5) + 32

print("Sua temperatura em Graus Fahrenheit: ", F)