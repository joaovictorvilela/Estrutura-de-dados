from random import shuffle

lista = list(range(0,10))

shuffle(lista)

def Mergesort(vetor, posicaoInicial, posicaoFinal):
    # condição de parada
    if posicaoInicial < posicaoFinal:
        # posição do elemento do meio
        metade_do_vetor = (posicaoInicial + posicaoFinal) // 2
        # quebrando o vetor em sub-vetor 1 (metade da esquerda)
        Mergesort(vetor, posicaoInicial, metade_do_vetor)
        # quebrando o vetor em sub-vetor 2 (metade da direita)
        Mergesort(vetor, metade_do_vetor+1, posicaoFinal)
        intercalar(vetor, posicaoInicial, metade_do_vetor, posicaoFinal)

def intercalar(vetor, posicaoInicial, metade_do_vetor, posicaoFinal):
    # cópia do vetor principal
    temp = vetor.copy() 
    # contador do sub-vetor 1
    i =  posicaoInicial
    # contador do sub-vetor 2
    j = metade_do_vetor + 1
    # contador do vetor principal
    k = posicaoInicial

    # momento que a intercalação será realizada
    while k <= posicaoFinal:
        # entra quando não tiver elementos no sub-vetor 1
        if i > metade_do_vetor:
            vetor[k] = temp[j]
            j += 1
        # entra quando não tiver elementos no sub-vetor 2
        elif j > posicaoFinal:
            vetor[k] = temp[i]
            i += 1
        # nesse caso retirar o elemento do sub-vetor 1
        elif temp[i] <= temp[j]:
            vetor[k] = temp[i]
            i += 1
        # nesse caso retirar o elemento do sub-vetor 2
        else:
            vetor[k] = temp[j]
            j += 1

        k += 1

Mergesort(lista,0,len(lista)-1)
print(lista)