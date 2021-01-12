lista = list(range(0,10))

def busca_sequencia(vetor, elementoProcurado):
    contador = 0

    while contador < len(vetor):
        if vetor[contador] == elementoProcurado:
            return contador

        contador += 1
    
    return -1


print(busca_sequencia(lista,5))