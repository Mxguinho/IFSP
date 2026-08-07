#D) Efetuar o cálculo da quantidade de litros de combustivel gasta em uma viagem, utilizando um automóvel que faz 12 quilômetros por litro. Para obter o cálculo, o usuário deve fornecer o tempo gasto (variável TEMPO) e a velocidade média (variável VELOCIDADE) durante a viagem. Dessa forma, será possível obter a distância percorrida com a fórmula DISTANCIA TEMPO VELOCIDADE. A partir do valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem com a fórmula LITROS USADOS DISTANCIA / 12. O programa deve apresentar os valores da velocidade média, tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem.

tempo = float(input("Digite o tempo gasto na viagem em horas: "))
velocidadeMedia = float(input("Digite a velocidade media da viagem: "))
distancia = velocidadeMedia * tempo
litros = distancia / 12

print("A quantidade de litros de combustivel gastos: ", litros)