from random import shuffle

lista = list(range(0,10))
shuffle(lista)

def quicksort(vetor, posicaoInicial, posicaoFinal):
    # condição de parada
    if posicaoInicial < posicaoFinal:
        pivo = particionar(vetor, posicaoInicial, posicaoFinal)
        # pivoltar a esquerda
        quicksort(vetor, posicaoInicial, pivo-1)
        # pivoltar a direita
        quicksort(vetor, pivo+1, posicaoFinal)


def particionar(vetor, posicaoInicial, posicaoFinal):
    # escolhendo o pivô (e o primeiro elemento da esquerda) 
    x = vetor[posicaoInicial]
    # destino final do pivô
    i = posicaoInicial
    # contador para percorrer o restante do vetor
    j = posicaoInicial + 1

    # percorrer o ventor 
    while j <= posicaoFinal:

        if vetor[j] < x:
            # detectou -se um elemento menor que o pivô, incremento o i
            i += 1 
            trocar(vetor, i, j)
        # passa oara o próximo elemento
        j += 1
    trocar(vetor, posicaoInicial, i)

    return i


def trocar(vetor, valor1, valor2):
    temp = vetor[valor1]
    vetor[valor1] = vetor[valor2]
    vetor[valor2] = temp


quicksort(lista,0,len(lista)-1)
print(lista)