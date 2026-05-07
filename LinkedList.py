from Node import Node
class LinkedList:
    def __init__(self):
        self.head = None
        self.contadorA = 201;
        self.contadorV = 1;

    def inserir(self):
        print('Informe a cor do cartão (A/V)')
        cor = (input())

        if cor == 'A':
            dado = self.contadorA
            self.contadorA += 1
            self.inserirComprioridade(dado, cor)
        elif cor == 'V':
            dado = self.contadorV
            self.contadorV += 1
            self.inserirSemPrioridade(dado, cor)
        else:
            print('Cor invalida')


    def inserirComprioridade(self, dado, cor):
        paciente = Node(dado, cor)

        if self.head is None:
            self.head = paciente
            return
        elif self.head.cor == 'V':
            auxi = self.head
            self.head = paciente
            paciente.proximo = auxi
            return

        atual = self.head
        while atual.proximo is not None and (atual.proximo.cor != 'V') :
            atual = atual.proximo

        auxi = atual.proximo
        atual.proximo = paciente
        paciente.proximo = auxi




    def inserirSemPrioridade(self,dado, cor):
        paciente = Node(dado, cor)

        if self.head is None: #caso a lista eteja vazia
            self.head = paciente
            return

        atual = self.head
        while atual.proximo:
            atual = atual.proximo

        atual.proximo = paciente

    def imprimirLista(self):
        lista = self.head
        print('Lista ->', end="")
        while lista is not None:
            print(f" [{lista.dado} - {lista.cor}] ", end="")
            lista = lista.proximo


    def atenderPcaciente(self):

        if self.head is None:
            print('Não existem pacientes na fila')
            return

        print(f"atendendo paciente {self.head.dado}, Cor: {self.head.cor}" )

        self.head = self.head.proximo