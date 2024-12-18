import matplotlib.pyplot as plt

def plotar_grafico(x, y):
    # Função para plotar um gráfico
    plt.figure(figsize=(8, 4))
    plt.plot(x, y, label="Seno")
    plt.title("Gráfico de Seno")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)
    plt.show()

def plotar_grafico_insertion_sort(n, g):
    # Plotar os resultados
    plt.figure(figsize=(12, 8))

    # Gráfico dos resultados empíricos
    plt.plot(n, g, '-', label='Testes Empíricos (Insertion Sort)', color='orange')

    # Gráficos das funções teóricas
    #plt.plot(n, f, 'r-', label='f(n) = 0.5n^2 + 3n')
    #plt.plot(n, g, 'b-', label='g(n) = n^2')

    # Adicionar elementos ao gráfico
    plt.title('Comparação dos Testes Empíricos e Funções Teóricas')
    plt.xlabel('Tamanho do Array (n)')
    plt.ylabel('Número de Atribuições (g)')
    plt.grid(True)
    plt.legend()

    # Mostrar o gráfico
    plt.show()