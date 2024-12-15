def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def algoritmo_de_insercao(o_array):
    for i in range(1, len(o_array)):
        chave = o_array[i] # pego o elemento do array que vou buscar, faço de chave ^
        j = i - 1 # pego o elemento anterior para comparar com a achave que
        
        # mover os elementos do array que sejam maiores que a chave (para uma posição acima)
        while j >= chave and o_array > chave: # enquanto j for maior ou igual a chave
                 o_array[j + 1] = o_array[j] # mova o elemento para a frente
                 j -= 1 # diminua o j
        o_array[j + 1] = chave
        
        
# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)
sorted_arr = insertion_sort(arr)
print("Sorted array:", sorted_arr)
