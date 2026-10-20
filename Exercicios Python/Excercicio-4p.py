# Criando um Dataframe a partir de um dicionario
dT = {
    'Nome':['Ana','Bruno', 'Carlos'],
    'idade': [25, 30, 22 ],
    'Cidade': ['sp', 'rj','bh']

}
df = pd.Dataframe(data)
# Visualizar as primeira linhas
print(df.head)