class Node:
    item = None
    proximo = None

    def __init__(self, item):
        self.item = item


class Lista_Encadeada:
    inicio  = None
    final   = None
    tamanho = 0

    def __init__(self):
        self.inicio = Node(None)
        self.final  = Node(None)

    # verificar se tá vazia
    def estaVazia(self):
        return self.tamanho == 0

    # inserir em uma posicao
    def inserir_em(self, item, pos) :
        if pos <= self.tamanho :
            p = self.inicio
            for i in range(pos) :
                p = p.proximo
            aux = Node(item)
            aux.proximo = p.proximo
            p.proximo = aux
            if pos == self.tamanho :
                self.final.proximo = aux
            self.tamanho += 1
        else:
            print('operacao invalida')

    # inserir no inicio
    def inserir_inicio(self, item):
        p = self.inicio
        aux = Node(item)
        aux.proximo = p.proximo
        p.proximo = aux
        if self.tamanho == 0:
            self.final.proximo = aux
        self.tamanho += 1

    # inserir no final sem sentinela
    '''
    def inserir_final(self, item):
        p = self.inicio
        for i in range(self.tamanho):
            p = p.proximo
        aux = Node(item)
        aux.proximo = p.proximo
        p.proximo = aux
        self.final.proximo = aux
        self.tamanho += 1
    '''
    # inserir no final com sentinela
    def inserir_final(self, item):
        p = self.final
        aux = Node(item)
        aux.proximo = None
        p.proximo = aux # proximo do atual 'no final'
        self.final = aux # novo final da lista
        if self.tamanho == 0 :
            self.inicio.proximo = aux
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

    # remover final sem sentinela
    # remover final com sentinela (duplamente encadeado...)
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
            #print("%s"  % (self.inicio.proximo.item))
            #print("%s"  % (self.final.proximo.item))
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

# main
lista = Lista_Encadeada()
lista.inserir_final('a')
lista.inserir_final('b')
lista.inserir_final('c')
lista.imprimir()
'''
lista.inserir_inicio('d')
#lista.inserir_em('e', 2)
#print("item: " + lista.remover_final())
lista.imprimir()

lista = Lista_Encadeada()
lista.inserir_final('a')
lista.inserir_final('b')
lista.inserir_final('c')
lista.inserir_final('d')
lista.imprimir() # a b c d
'''

























# class Celula:
# 	item = None
# 	proximo = None

# 	def __init__(self,item):
# 		self.item = item

# class Lista_Encadeada:
# 	inicio = None
# 	tamanho = 0

# 	def __init__(self):
# 		self.inicio = Celula(None)		

# 	def estaVazia(self):
# 		return self.tamanho == 0

# 	def inserir(self,item,pos):
# 		if pos<=self.tamanho:
# 			p = self.inicio
# 			#encontrar a celula anterior a pos
# 			for i in range(pos):
# 				p = p.proximo
# 			aux = Celula(item)
# 			aux.proximo = p.proximo
# 			p.proximo = aux
# 			self.tamanho +=1

# 	def remover(self,pos):
# 		if not self.estaVazia() and pos < self.tamanho:
# 			p = self.inicio
# 			for i in range(pos):
# 				p = p.proximo
# 			aux = p.proximo
# 			p.proximo = aux.proximo
# 			item = aux.item
# 			del aux
# 			self.tamanho -=1
# 			return item
# 		else:
# 			print('operacao invalida')
			
		

# 	def imprimir(self):
# 		p = self.inicio.proximo
# 		while p!= None:
# 			print(p.item)
# 			p = p.proximo
# 		print('---')

		

# 	# def buscar(self,item):
# 		#retornar posicao do item se ele existir

# 	# def removerI(self,item):
# 		#remover o item se ele existir

# lista = Lista_Encadeada()
# lista.inserir('a',0)
# lista.inserir('b',1)
# lista.inserir('c',2)
# lista.inserir('d',3)
# lista.inserir('e',4)
# lista.imprimir()
# lista.inserir('h',2)
# lista.imprimir()
# lista.remover(5)
# lista.remover(4)
# lista.remover(3)
# lista.remover(2)
# lista.remover(1)
# lista.remover(0)
# lista.imprimir()
# lista.inserir('h',0)
# lista.imprimir()
