import numpy as np
import random

def gerar_dados():
    # Função para gerar dados fictícios
    x = np.linspace(5, 20, 50)
    y = np.sin(x)
    return x, y

# Definir o intervalo de tamanhos para n
# n = np.arange(1, 501, 10)  # Gera entrada: 1, 11, 21, ..., 491

# Função de ordenação com contagem de atribuições
def gerar_insertion_sort(arr):
    t = 0 
    for i in range(1, len(arr)): 
        chave = arr[i]
        t += 1 
        j = i - 1 
        while j >= 0 and arr[j] > chave:
            arr[j + 1] = arr[j] 
            t += 1
            j -= 1 
        arr[j + 1] = chave
        t += 1
    return t

def gerar_dados_insertion():
    n = np.arange(1, 501, 10)
    g = []
    for t in n:
        lista_numeros = [random.randint(1, 1000) for _ in range(t)]
        a = gerar_insertion_sort(lista_numeros) 
        g.append(a)

    return t, g