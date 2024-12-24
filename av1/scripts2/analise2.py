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
    f_de_n_aleatorio = []
    f_de_n_crescente = []
    f_de_n_decrescente = []

    for t in n:
        lista_numeros = [random.randint(1, 1000) for _ in range(t)]
        lista_crescente = sorted(lista_numeros)
        lista_decrescente = sorted(lista_numeros, reverse=True)

        a_aleatorio = gerar_insertion_sort(lista_numeros)
        a_crescente = gerar_insertion_sort(lista_crescente)
        a_decrescente = gerar_insertion_sort(lista_decrescente)

        f_de_n_aleatorio.append(a_aleatorio)
        f_de_n_crescente.append(a_crescente)
        f_de_n_decrescente.append(a_decrescente)

    return n, f_de_n_aleatorio, f_de_n_crescente, f_de_n_decrescente