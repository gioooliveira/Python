import pandas as pd
#Não esquecçam de instalar via prompt do dos a biblioteca openpyxl
# Caminho do arquivo

#arquivo ='"C:\Users \Aluno\Desktop\Funcionario.xlsx"

arquivo = "C:/Users/aluno/Desktop/Pasta1.xlsx"

#ler uma planilha especiica

df = pd.read_excel(arquivo,sheet_name='Planilha1')

print(df)
