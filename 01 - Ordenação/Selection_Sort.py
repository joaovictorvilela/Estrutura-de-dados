from random import shuffle

lista = list(range(0,10))
shuffle(lista)

def Selection_Sort(vetor):
    i = 0
    while i < len(vetor) - 1:
        menor = i
        j = i + 1
        # em busca do menor elemento
        while j < len(vetor):
            if vetor[j] < vetor[menor]:
                menor = j
            j += 1
        
        if menor != i:
            temp = vetor[i]
            vetor[i] = vetor[menor]
            vetor[menor] = temp

        i += 1

Selection_Sort(lista)
print(lista)