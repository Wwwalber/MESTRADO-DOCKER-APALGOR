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