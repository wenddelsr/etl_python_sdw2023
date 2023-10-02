# Projeto ETL (Extração, Transformação e Carregamento) para Santander Bootcamp 2023 - Ciência de Dados com Python

Este é um projeto de exemplo que demonstra o processo ETL (Extração, Transformação e Carregamento) em Python. O objetivo é extrair dados de fontes de dados em formatos CSV e JSON, transformar esses dados calculando risco e sugerindo investimentos, e carregar os dados transformados em novos arquivos CSV e JSON.

## Passos do Projeto

1. **Extração dos Dados:**
   - Os dados de clientes são extraídos de um arquivo CSV (dados.csv) e de um arquivo JSON (dados.json) usando a biblioteca pandas.

2. **Transformação dos Dados:**
   - É calculado o nível de risco com base no saldo da conta dos clientes.
   - Com base no risco calculado, são feitas sugestões de investimento.
   - As informações de risco e sugestão de investimento são adicionadas aos dados.

3. **Carregamento:**
   - Os dados transformados com informações de risco e sugestão de investimento são salvos em novos arquivos CSV (clientes_com_sugestao_risco.csv) e JSON (clientes_com_sugestao_risco.json).

## Como Executar

Para executar o projeto, você precisa ter Python instalado e as bibliotecas pandas. Você pode seguir os seguintes passos:

1. Clone este repositório para o seu computador.
2. Certifique-se de que os arquivos `clientes.csv` e `clientes.json` estão presentes na pasta.
3. Execute o script Python `etl.py` usando o comando `python etl.py`.

## Exemplo de Saída

O resultado do projeto inclui um novo arquivo CSV (clientes_com_sugestao_risco.csv) e um novo arquivo JSON (clientes_com_sugestao_risco.json) contendo os dados transformados com informações de risco e sugestão de investimento.

Este é um projeto simples que pode ser expandido e personalizado para atender a requisitos específicos. É um exemplo de como realizar o processo ETL em Python para análise de dados e tomada de decisões com base nas informações extraídas e transformadas.