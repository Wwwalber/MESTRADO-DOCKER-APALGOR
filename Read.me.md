Estrutura atual:

Copy.
├── av1/          # Sincronizado com /app/av1 no container
├── av2/          # Sincronizado com /app/av2 no container
├── av3/          # Sincronizado com /app/av3 no container
├── Dockerfile
├── docker-compose.yml
└── requirements.txt

Importante lembrar:

O ambiente Python e todas as bibliotecas estão no container
Os arquivos são compartilhados através dos volumes
Você pode parar/iniciar o container sem perder seus arquivos
Para instalar novas bibliotecas, você precisa:

Adicionar ao requirements.txt
Reconstruir o container: docker-compose up --build -d

Esta configuração é muito útil porque:

Mantém seu ambiente Python isolado e reproduzível
Permite trabalhar com os arquivos normalmente no seu computador
Fornece um ambiente Jupyter completo com todas as bibliotecas necessárias
Torna fácil compartilhar o ambiente com outras pessoas