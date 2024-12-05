# Usa a imagem oficial do Python, versão slim para um ambiente leve
FROM python

# Atualiza pacotes e instala algumas dependências básicas
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Configura o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo de requerimentos (definido abaixo) para o contêiner
COPY requirements.txt .

COPY . .

# Instala as bibliotecas necessárias
RUN pip install --no-cache-dir -r requirements.txt

# cria o arquivo de configuração do Jupyre Notebook
RUN mkdir -p /root/.jupyter && \
    echo "c.NotebookApp.token = ''" >> /root/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.password = ''" >> /root/.jupyter/jupyter_notebook_config.py

    # Configurar variáveis de ambiente
ENV PYTHONUNBUFFERED=1

# Expõe a porta do Jupyter
EXPOSE 8888

# Comando para iniciar o Jupyter Notebook (opcional)
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
