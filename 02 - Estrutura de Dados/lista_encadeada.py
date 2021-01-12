class Node:
    item = None
    proximo = None

    def __init__(self, item):
        self.item = item


class Lista_Encadeada:
    inicio = None
    tamanho = 0

    def __init__(self):
        self.inicio = Node(None)

    # verificar se tá vazia
    def estaVazia(self):
        return self.tamanho == 0

    # inserir em uma posicao
    def inserir_em(self, item, pos):
        if pos <= self.tamanho:
            p = self.inicio
            for i in range(pos):
                p = p.proximo
            aux = Node(item)
            aux.proximo = p.proximo
            p.proximo = aux
            self.tamanho += 1
        else:
            print('operacao invalida')

    # inserir no inicio
    def inserir_inicio(self, item):
        p = self.inicio
        aux = Node(item)
        aux.proximo = p.proximo
        p.proximo = aux
        self.tamanho += 1

    # inserir no final
    def inserir_final(self, item):
        p = self.inicio
        for i in range(self.tamanho):
            p = p.proximo
        aux = Node(item)
        aux.proximo = p.proximo
        p.proximo = aux
        self.tamanho += 1
	
    # remover da posicao
    def remover_posicao(self, pos):
        if not self.estaVazia() and pos<self.tamanho:
            p = self.inicio
            for i in range(pos):
                p = p.proximo
            aux = p.proximo
            p.proximo = aux.proximo
            item = aux.item
            del aux
            self.tamanho -=1
            return item
        else:
            print('operacao invalida')

    # remover inicio
    def remover_inicio(self):
        if not self.estaVazia() :
            p = self.inicio
            aux = p.proximo
            self.inicio = self.inicio.proximo
            item = aux.item
            del aux
            self.tamanho -=1
            return item
        else:
            print('operacao invalida')

    # remover final
    def remover_final(self):
        if not self.estaVazia() :
            p = self.inicio
            while ((p.proximo).proximo != None) :
                p = p.proximo
            aux = p.proximo
            p.proximo = aux.proximo
            item = aux.item
            del aux
            self.tamanho -=1
            return item
        else:
            print('operacao invalida')

    # imprimir
    def imprimir(self):
        p = self.inicio
        for i in range(self.tamanho):
            p = p.proximo
            print(p.item)
        print('---')

    # buscar por item
    def buscarPorItem(self, item):
        p = self.inicio
        for i in range(self.tamanho):
            p = p.proximo
            if p.item == item:
                return i
        return None

    # buscar por posicao
    def buscaPorPosicao(self, pos):
        p = self.inicio.proximo
        for i in range(pos):
            p = p.proximo
        return p.item