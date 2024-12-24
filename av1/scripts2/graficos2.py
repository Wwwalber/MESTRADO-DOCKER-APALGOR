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

def plotar_grafico_insertion_sort(n, f_de_n_aleatorio, f_de_n_crescente, f_de_n_decrescente, titulo="Gráfico de Insertion Sort"):
    plt.figure(figsize=(10, 6))
    plt.plot(n, f_de_n_aleatorio, label='Dados Aleatórios')
    plt.plot(n, f_de_n_crescente, label='Dados Crescentes')
    plt.plot(n, f_de_n_decrescente, label='Dados Decrescentes')
    plt.xlabel('Tamanho do vetor (n)')
    plt.ylabel('Tempo de execução (f(n))')
    plt.title(titulo)
    plt.legend()
    plt.grid(True)
    plt.show()