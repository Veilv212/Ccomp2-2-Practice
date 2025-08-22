
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        menores = []
        mayores = []
        
        for i in range(1,len(lista)):
            if lista[i] <= pivote:
                menores.append(lista[i])
            else:
                mayores.append(lista[i])
        return quicksort(menores) + [pivote] + quicksort(mayores)
    
mi_lista = [5, 2, 10, 83, 21]
ordenada = quicksort(mi_lista)
print(ordenada)
