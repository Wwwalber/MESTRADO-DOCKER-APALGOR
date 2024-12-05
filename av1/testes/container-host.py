# Este código rodará no container mas o arquivo será salvo em ambos os lugares
# Dentro do Jupyter Notebook
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': np.random.rand(10),
    'B': np.random.rand(10)
})

# Salvar em av1
df.to_csv('/app/av1/dados.csv')