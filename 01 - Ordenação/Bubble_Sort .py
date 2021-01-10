from random import shuffle # importando o shuffle do módulo random

lista = list(range(0,10))

shuffle(lista) # embaralhando os números

def bubble_sort(vetor):
    # verificando a quantidade de elementos, para decrementar a variável
    fim = len(vetor)
    # enquanto a lista tiver um tamanho
    while fim > 0:

        i = 0
        # percorrendo o vetor de 0 até fim
        while i < fim-1:
            if vetor[i] > vetor[i+1]:
                # realizando a troca da posição atual com a próxima
                temp = vetor[i]
                vetor[i] = vetor[i+1]
                vetor[i+1] = temp
            i += 1
            
        fim -= 1

bubble_sort(lista)
print(lista)