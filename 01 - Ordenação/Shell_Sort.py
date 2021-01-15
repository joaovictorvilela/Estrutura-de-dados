from random import shuffle

lista = list(range(0,10))
shuffle(lista)

def Shell_Sort(vetor):
    distancia = len(vetor) // 2
    while distancia > 0:
        i = distancia
        while i < len(vetor):
            temp = vetor[i]
            trocou = False
            j = i - distancia
            while j >= 0 and vetor[j] > temp:
                vetor[j+distancia] = vetor[j]
                trocou = True
                j -= distancia
            
            if trocou:
                vetor[j+distancia] = temp
        
            i += 1
        
        distancia //= 2

Shell_Sort(lista)
print(lista)