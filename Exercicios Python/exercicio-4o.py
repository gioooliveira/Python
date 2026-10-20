#DATAFRAME  em python
import pandas as pd


#Criando um Dtaframe a partir de um dicionario 
data = {
    'Nome':['Inacio','José', 'Eduardo'],
        'idade': [56, 77, 91 ],
        'Cidade': ['BA', 'RS', 'PE']

}

df = pd.DataFrame(data)

print(df[[ 'Nome', 'Cidade']])