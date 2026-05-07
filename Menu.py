import LinkedList

lista = LinkedList.LinkedList()
while True:
    print("\n")
    print('1 - Adicionar paciente a fila')
    print('2 - Mostrar paciente na fila')
    print('3 - Chamar paciente')
    print('4 - Sair')

    op = int(input())
    if op == 4:
        print('Programa encerrado')
        break
    elif op == 1:
        lista.inserir()
    elif op == 2:
        lista.imprimirLista()

    elif op == 3:
       lista.atenderPcaciente()
    else:
        print('opção invalida')
