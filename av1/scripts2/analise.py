import numpy as np

def gerar_dados():
    # Função para gerar dados fictícios
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    return x, y