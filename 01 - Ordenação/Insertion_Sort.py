from random import shuffle

lista = list(range(0,10))
shuffle(lista)

def Insertion_Sort(vetor):
    i = 1
    while i < len(vetor):
        temp = vetor[i]
        trocou = False
        j = i - 1
        while j >= 0 and vetor[j] > temp:
            vetor[j+1] = vetor[j]
            trocou = True
            j -= 1
        
        if trocou:
            vetor[j+1] = temp
    
        i += 1

Insertion_Sort(lista)
print(lista)