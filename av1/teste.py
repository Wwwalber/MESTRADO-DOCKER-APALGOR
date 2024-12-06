import numpy as np
import matplotlib.pyplot as plt

# Criar um array de valores para n
n = np.linspace(0, 10, 100)  # Cria 100 pontos entre 0 e 10

# Calcular os valores das funções
f = n**2 + 2*n      # f(n) = n² + 2n
g = n**2            # g(n) = n²
h = 2*n + 1         # h(n) = 2n + 1

# Criar o gráfico
plt.figure(figsize=(10, 6))  # Define o tamanho da figura

# Plotar cada função
plt.plot(n, f, 'r-', label='f(n) = n² + 2n')
plt.plot(n, g, 'b-', label='g(n) = n²')
plt.plot(n, h, 'g-', label='h(n) = 2n + 1')

# Adicionar elementos ao gráfico
plt.title('Comparação das Funções')
plt.xlabel('n')
plt.ylabel('f(n), g(n), h(n)')
plt.grid(True)
plt.legend()

# Mostrar o gráfico
plt.show()