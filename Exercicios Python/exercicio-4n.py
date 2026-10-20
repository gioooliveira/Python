#DATAFRAME em python 
import pandas as pd

# Criando um DATAFRAME a partir de um dicionario
data = {
    'Nome':['Ana', 'Bruno', 'Carlos'],
    'Idade': [25, 30, 22],
    'Cidade': ['SP', 'RJ', 'BH']

}
df = pd.DataFrame(data)

# Exibindo o Dataframe
print(df)

#Acessando uma coluna
print('Nome')

#filtrando dados (idade > 23)
print(df[df['Idade'] > 23])