import pandas as pd

# Carregando dados do CSV e JSON
df_csv = pd.read_csv('dados.csv')
df_json = pd.read_json('dados.json')

# Função para calcular o risco baseado no saldo da conta
def calcular_risco(saldo):
    if saldo > 5000:
        return 'Baixo Risco'
    elif saldo > 2000:
        return 'Médio Risco'
    else:
        return 'Alto Risco'

# Adicionando uma coluna de Risco aos dados do CSV
df_csv['Risco'] = df_csv['Saldo da conta'].apply(calcular_risco)

# Função para sugerir diversificação de investimentos
def sugerir_investimento(row):
    if row['Risco'] == 'Baixo Risco':
        return 'Investimento em Fundos de Renda Fixa'
    elif row['Risco'] == 'Médio Risco':
        return 'Investimento em Fundos Diversificados'
    else:
        return 'Poupança'

# Adicionando uma coluna de Sugestão de Investimento
df_csv['Sugestão de Investimento'] = df_csv.apply(sugerir_investimento, axis=1)

# Salvando os dados transformados em um novo arquivo CSV
df_csv.to_csv('clientes_com_sugestao_risco.csv', index=False)

# Salvando os dados transformados em um novo arquivo JSON
df_json['Risco'] = df_json['Saldo da conta'].apply(calcular_risco)
df_json['Sugestão de Investimento'] = df_json.apply(sugerir_investimento, axis=1)
df_json.to_json('clientes_com_sugestao_risco.json', orient='records')