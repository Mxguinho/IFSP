import professor as p

i = 1
opções = {1, 2, 3, 4, 5, 6}
while i != 0:
    print("Digite a opção desejada: ")
    print("1 = cadastrar professor")
    print("2 = listar professores")
    print("3 = buscar professor id")
    print("4 = buscar professor nome")
    print("5 = alterar professor")
    print("6 = excluir professor")
    print("0 = sair")
    i = int(input("Opção: ")[0])

    match i:
        case 1:
            p.cadastrar_professor()
        case 2:
            p.listar_professores()
        case 3:
            p.buscar_professor_id()
        case 4:
            p.buscar_professor_nome()
        case 5:
            p.alterar_professor()
        case 6:
            p.excluir_professor()
        case 0:
            print("Operação finalizada!!!")
        case _:
            i = 0
            print("Operação finalizada!!!")

    if i in opções:
        input("Pressione ENTER para continuar...")
