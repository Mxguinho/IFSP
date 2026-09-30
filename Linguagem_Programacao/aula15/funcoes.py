def caracteres(texto):
    return len(texto.replace(" ", ""))

def caracteres2(texto):
    i = 0
    for c in texto:
        if c != " ":
            i += 1
    return i

def inverter(texto):
    texto_invertido = ""
    for c in texto:
        texto_invertido = c + texto_invertido
    return texto_invertido

def vogais(texto):
    i = 0
    for c in texto.lower():
        if c == "a" or c == "e" or c == "i" or c == "o" or c == "u": #não pega com acento
            i += 1
    return i

def vogais2(texto):
    i = 0
    vogal = "aeiouáéíóúàèìòùãõâêîôû"
    for c in texto.lower():
        if c in vogal:
            i += 1
    return i

def fibonacci(num):
    n = []
    n.append(0)
    n.append(1)
    if(num == 1):
        return n[:1]
    elif(num == 2):
        return n[:]
    else:
        for i in range(num - 2):
            n.append(n[i] + n[i + 1])
        return n
