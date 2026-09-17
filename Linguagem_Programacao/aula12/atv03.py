senha = input("Digite sua senha: ")
maiusculo = 0
minusculo = 0


# senha.isupper #tem maiuscula
# senha.islower #tem minuscula
# senha.isdigit #tem numero

if len(senha) <  8:
    print("a senha tem menos de 8 caracteres")
elif any(senha.islower() for char in senha):
    print("a senha não tem minusculo")
elif any(senha.isupper() for char in senha):
    print("a senha não tem maiusculo")
elif any(senha.isdigit() for char in senha):
    print("não tem nenhum numero")
else:
    print("Senha valida")