import matplotlib.pyplot as plt
import numpy as np
import time

# função para coletar tempo de execução
def medindo_tempo(sizes):
    times = []
    for n in sizes:
        # cria uma lista com n elementos
        lista = list(range(n))
        
        # mede o tempo de execução
        inicio = time.perf_counter()
        
        # executa insertion_sort(lista)
        
        fim = time.perf_counter()
        # calcula o tempo de execução
        tempo = fim - inicio
        times.append(tempo)
    return times
