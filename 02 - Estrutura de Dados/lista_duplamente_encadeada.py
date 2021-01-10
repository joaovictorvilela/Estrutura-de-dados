class Node(object):

    def __init__(self, item, anterior, proximo):
        self.item     = item
        self.anterior = anterior
        self.proximo  = proximo

    def __str__(self) :
        return str(self.item)
 
 
class ListaDuplamenteEncadeada(object):
    inicio  = None
    tamanho = 0

    def __init__(self):
        self.inicio  = Node(None, None, None)
        self.tamanho = 0

    # verificar se tá vazia
    def estaVazia(self):
        return self.tamanho == 0

    # inserir em uma posicao
    def inserir_em(self, item, pos):
        if pos <= self.tamanho:
            p = self.inicio
            for i in range(pos):
                p = p.proximo
            aux = Node(item, p, p.proximo)
            p.proximo = aux
            if (aux.proximo != None) :
                aux.proximo.anterior = aux
            self.tamanho += 1
        else:
            print('operacao invalida')

    # inserir no inicio
    def inserir_inicio(self, item):
        self.inserir_em(item, 0)

    # inserir no final
    def inserir_final(self, item):
        self.inserir_em(item, self.tamanho)

    # remover da posicao
    def remover_posicao(self, pos):
        if not self.estaVazia() and pos < self.tamanho:
            p = self.inicio
            for i in range(pos):
                p = p.proximo
            aux = p.proximo
            p.proximo = aux.proximo
            if (aux.proximo != None) : 
                aux.proximo.anterior = p
            item = aux.item
            del aux
            self.tamanho -=1
            return item
        else:
            print('operacao invalida')

    # remover inicio
    def remover_inicio(self):
        self.remover_posicao(0)

    # remover final
    def remover_final(self):
        self.remover_posicao(self.tamanho-1)

    # imprimir
    def imprimir(self):
        p = self.inicio
        for i in range(self.tamanho):
            p = p.proximo
            #print("%s %s %s" % (p.anterior, p.item, p.proximo))
            print("%s" % (p.item))
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

lista = ListaDuplamenteEncadeada()
 
lista.inserir_final(2)
lista.inserir_final(5)
lista.inserir_final(12)
lista.inserir_final(6)
lista.inserir_final(20)
lista.imprimir()

print("Encontrado na posição: " + str(lista.buscarPorItem(12)))
print("Encontrado o item: " + str(lista.buscaPorPosicao(4)))

lista.remover_posicao(1)
lista.imprimir()
lista.remover_inicio()
lista.imprimir()
lista.remover_final()
lista.imprimir()

