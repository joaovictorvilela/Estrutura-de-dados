lista = list(range(0,10))

def busca_sequencial_sentinela(vetor, elementoProcurado):
    posicao = 0
    # adicionando uma sentinela
    vetor.append(elementoProcurado)
    # percorrendo o vetor
    while vetor[posicao] != elementoProcurado:
        posicao += 1
        
    if posicao == len(vetor) - 1:
        return -1

    return posicao

print(busca_sequencial_sentinela(lista,20))