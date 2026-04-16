# O dataset LOGCP - base_tickets_manutencao_historico.xlsx contém o histórico de incidentes da empresa.
# Através da importantação dos dados através da biblioteca pandas, responda as perguntas abaixo.
# 1 - (1,0) Quantos tickets foram (utilize a coluna "des_status"):
#    - Abertos?
#    - Concluídos?
#    - Cancelados?
# 2 - (1,0) Qual a taxa de conclusão dos tickets em relação ao total?
# 3 - (1,0) Qual categoria tem mais tickets(utilize a coluna "des_categoria")?
# 4 - (1,0) Qual categoria tem maior numero de de cancelamento?

# 5 - (1,0) Quanto rendeu a VALE3 nos ultimos 5 anos entre 2020 e 2025?
# base_url = "https://laboratoriodefinancas.com/api/v2"
# token = "SEU_JWT"
# params = {"ticker": "VALE3", "data_ini": "2001-01-01", "data_fim": "2026-12-31"}
# response = requests.get(
#     f"{base_url}/preco/corrigido",
#     headers={"Authorization": f"Bearer {token}"},
#     params=params,
# )

# 6 - (1,0) A BrasilAPI disponibiliza informações da tabela FIPE, incluindo marcas, modelos e preços de veículos.
# Acesse o endpoint de marcas da FIPE para o tipo de veículo carros.
# import requests
# import pandas as pd
# tipoVeiculo = "carros"
# api = f"https://brasilapi.com.br/api/fipe/marcas/v1/{tipoVeiculo}"
# Transforme em DataFrame e acha o codigo BYD através da coluna "nome"
# Use esse código para acessar o endpoint de modelos da marca BYD.
# codigoMarca=""
# api = f"https://brasilapi.com.br/api/fipe/veiculos/v1/{tipoVeiculo}/{codigoMarca}"
# Construa um DataFrame com os modelos disponíveis.
# Responda: quantos modelos de veículos BYD estão cadastrados na FIPE?

# 7 - (1,0) O Banco Mundial disponibiliza uma API pública com diversos indicadores econômicos. 
# O código do indicador NY.GDP.PCAP.CD corresponde ao PIB per capita (em dólares correntes).
# Usando Python e a biblioteca requests para acessar a API e pandas para manipulação dos dados:
# Acesse o indicador "NY.GDP.PCAP.CD" e o pais "BRA".
# url = f"https://api.worldbank.org/v2/country/{pais}/indicator/{indicador}?format=json"
# Construa um DataFrame atraves do segundo elemento da lista do retorno
# Selecione apenas as colunas anos (date) e os valores de PIB per capita (value).
# Identifique em qual ano o Brasil apresentou o menor PIB per capita e mostre o respectivo valor.


# 8 - (1,0) - Faça um ranking das 30 melhores empresas baseado nos indicadores Return on Equity (roe) e Dividend Yield (dividend_yield) no dia 2024-04-01.
# Faça uma média entre o ranking das empresas com maior ROE e o ranking das empresas com maior dividend_yield
# base_url = "https://laboratoriodefinancas.com/api/v2"
# token = "SEU_JWT"
# response = requests.get(
#     f"{base_url}/bolsa/planilhao",
#     headers={"Authorization": f"Bearer {token}"},
#     params={"data_base": "2026-04-01"},
# )

# 9 - (1,0) Quantos setores ("setor") tem essa carteira formada por 30 ações?


# 10 - (1,0) 11 - Você tem acesso à API do Laboratório de Finanças, que fornece dados do Planilhão em formato JSON. 
# Selecione a empresa do setor de "varejo" que apresenta o maior endividamento na data base 2024-04-01.
# Exiba APENAS AS COLUNAS "ticker", "setor", "preco", "endividamento"
# base_url = "https://laboratoriodefinancas.com/api/v2"
# token = "SEU_JWT"
# response = requests.get(
#     f"{base_url}/bolsa/planilhao",
#     headers={"Authorization": f"Bearer {token}"},
#     params={"data_base": "2026-04-01"},
# )


# 11 - (1,0) O IPEA disponibiliza uma API pública com diversas séries econômicas.
# Para localizar uma série de interesse, é necessário acessar primeiro o endpoint de metadados.
# Acesse o endpoint de metadados:
# "http://www.ipeadata.gov.br/api/odata4/Metadados"
# Transforme o retorno em um DataFrame.
# Filtre para encontrar as séries do IBGE relacionadas à taxa de desemprego no Brasil.
# Dica:
# - Utilize a coluna FNTSIGLA para encontrar as séries do "IBGE";
# - Utilize a coluna SERNOME para encontrar as séries relacionadas a "Taxa de desemprego - cor negra"


# 12 - (1,0) Descubra qual é o código da série correspondente (coluna: SERCODIGO).
# CODIGO_ENCONTRADO = ''
# Usando o código encontrado, acesse a API de valores:
# f"http://ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='{CODIGO_ENCONTRADO}')"
# Construa um DataFrame a partir da chave 'value' do retorno da API.
# Selecione apenas as colunas de data (VALDATA) e valor (VALVALOR).
# Exiba a Data e o Valor em que a taxa de desemprego atingiu o maior valor da série.

import pandas as pd
import requests

# ============ QUESTAO 1-4: LOGCP Análise Tickets ============
file_path = "base_tickets_manutencao_historico.xlsx"
df_tickets = pd.read_excel(file_path)

# Questao 1: Contar tickets
print("=== QUESTAO 1 ===")
status_counts = df_tickets["des_status"].value_counts()
print(f"Abertos: {status_counts.get('Abertos', 0)}")
print(f"Concluídos: {status_counts.get('Concluídos', 0)}")
print(f"Cancelados: {status_counts.get('Cancelados', 0)}")

# Questao 2: Taxa de conclusão
print("\n=== QUESTAO 2 ===")
total_tickets = len(df_tickets)
completed = len(df_tickets[df_tickets["des_status"] == "Concluídos"])
completion_rate = (completed / total_tickets) * 100
print(f"Taxa de conclusão: {completion_rate:.2f}%")

# Questao 3: Categoria com mais tickets
print("\n=== QUESTAO 3 ===")
category_counts = df_tickets["des_categoria"].value_counts()
top_category = category_counts.idxmax()
print(f"Categoria com mais tickets: {top_category} ({category_counts[top_category]} tickets)")

# Questao 4: Categoria com mais cancelamentos
print("\n=== QUESTAO 4 ===")
canceled_df = df_tickets[df_tickets["des_status"] == "Cancelados"]
canceled_by_category = canceled_df["des_categoria"].value_counts()
top_canceled_category = canceled_by_category.idxmax()
print(f"Categoria com mais cancelamentos: {top_canceled_category} ({canceled_by_category[top_canceled_category]} cancelamentos)")

# ============ QUESTAO 5: VALE3 Quanto rendeu ============
print("\n=== QUESTAO 5 ===")
base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc4OTI5NTIxLCJpYXQiOjE3NzYzMzc1MjEsImp0aSI6IjVhYjAxODkzN2NmZDRkNTc5MTZiZWE1Y2JkMzI5NGI0IiwidXNlcl9pZCI6IjEwMiJ9.yMnN8pBeJZJ2GTf-KEEQGkB-0m7mOrFFfIyNUwHP7Tc"
params = {"ticker": "VALE3", "data_ini": "2020-01-01", "data_fim": "2025-12-31"}
try:
    response = requests.get(
        f"{base_url}/preco/corrigido",
        headers={"Authorization": f"Bearer {token}"},
        params=params,
    )
    if response.status_code == 200:
        vale3_data = response.json()
        df_vale3 = pd.DataFrame(vale3_data)
        total_return = ((df_vale3.iloc[-1]["preco"] - df_vale3.iloc[0]["preco"]) / df_vale3.iloc[0]["preco"]) * 100
        print(f"Rendimento VALE3 (2020-2025): {total_return:.2f}%")

# ============ QUESTAO 6: BYD Veiculos pela FIPE ============
print("\n=== QUESTAO 6 ===")
tipo_veiculo = "carros"
try:
    # Pegar as marcas
    api_marcas = f"https://brasilapi.com.br/api/fipe/marcas/v1/{tipo_veiculo}"
    response_marcas = requests.get(api_marcas)
    df_marcas = pd.DataFrame(response_marcas.json())
    
    # Encontrar o código da BYD
    codigo_byd = df_marcas[df_marcas["nome"] == "BYD"]["codigo"].values[0]
    
    # Pegar os modelos BYD
    api_modelos = f"https://brasilapi.com.br/api/fipe/veiculos/v1/{tipo_veiculo}/{codigo_byd}"
    response_modelos = requests.get(api_modelos)
    df_modelos = pd.DataFrame(response_modelos.json())
    
    num_modelos = len(df_modelos)
    print(f"Modelos BYD cadastrados na FIPE: {num_modelos}")

# ============ QUESTAO 7: World Bank GDP Per Capita ============
print("\n=== QUESTAO 7 ===")
pais = "BRA"
indicador = "NY.GDP.PCAP.CD"
try:
    url = f"https://api.worldbank.org/v2/country/{pais}/indicator/{indicador}?format=json"
    response = requests.get(url)
    data = response.json()
    df_gdp = pd.DataFrame(data[1])
    
    # Selecionar colunas e limpar dados
    df_gdp_clean = df_gdp[["date", "value"]].dropna()
    df_gdp_clean["value"] = pd.to_numeric(df_gdp_clean["value"])
    
    # Encontrar o menor PIB per capita
    min_idx = df_gdp_clean["value"].idxmin()
    min_year = df_gdp_clean.loc[min_idx, "date"]
    min_value = df_gdp_clean.loc[min_idx, "value"]
    
    print(f"Menor PIB per capita: {min_year} - R${min_value:.2f}")


# ============ QUESTAO 8-10: Análise Planilhao ============
print("\n=== QUESTAO 8 ===")
try:
    response = requests.get(
        f"{base_url}/bolsa/planilhao",
        headers={"Authorization": f"Bearer {token}"},
        params={"data_base": "2024-04-01"},
    )
    if response.status_code == 200:
        planilhao_data = response.json()
        df_planilhao = pd.DataFrame(planilhao_data)
        
        # Questao 8: Ranking pelo ROE e Dividendo Yield
        df_top30 = df_planilhao.nlargest(30, "roe")
        df_top30["roe_rank"] = df_top30["roe"].rank(ascending=False)
        df_top30["dividend_rank"] = df_top30["dividend_yield"].rank(ascending=False)
        df_top30["avg_rank"] = (df_top30["roe_rank"] + df_top30["dividend_rank"]) / 2
        df_ranked = df_top30.sort_values("avg_rank")
        print("Top 10 empresas por ranking combinado:")
        print(df_ranked[["ticker", "roe_rank", "dividend_rank", "avg_rank"]].head(10))
        
        # Questao 9: Numero dos setores na carteira
        print("\n=== QUESTAO 9 ===")
        num_setores = df_ranked["setor"].nunique()
        print(f"Número de setores na carteira: {num_setores}")
        
        # Questao 10: Maior endividamento no setor de varejo
        print("\n=== QUESTAO 10 ===")
        df_varejo = df_planilhao[df_planilhao["setor"] == "varejo"]
        empresa_maior_endividamento = df_varejo.loc[df_varejo["endividamento"].idxmax()]
        resultado = df_varejo[df_varejo["endividamento"] == df_varejo["endividamento"].max()][["ticker", "setor", "preco", "endividamento"]]
        print(resultado)


# ============ QUESTAO 11-12: IPEA Desemprego ============
print("\n=== QUESTAO 11 ===")
try:
    url_meta = "http://www.ipeadata.gov.br/api/odata4/Metadados"
    response = requests.get(url_meta)
    data_meta = response.json()
    df_meta = pd.DataFrame(data_meta["value"])
    
    # Filtrar séries do IBGE sobre o desemprego
    df_desemprego = df_meta[
        (df_meta["FNTSIGLA"] == "IBGE") & 
        (df_meta["SERNOME"].str.contains("Taxa de desemprego - cor negra", na=False))
    ]
    print(f"Séries encontradas: {len(df_desemprego)}")
    
    # Questao 12: Maior taxa de desemprego
    print("\n=== QUESTAO 12 ===")
    if len(df_desemprego) > 0:
        codigo_encontrado = df_desemprego.iloc[0]["SERCODIGO"]
        url_valores = f"http://ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='{codigo_encontrado}')"
        response_valores = requests.get(url_valores)
        data_valores = response_valores.json()
        df_valores = pd.DataFrame(data_valores["value"])
        
        # Converter os valores
        df_valores_clean = df_valores[["VALDATA", "VALVALOR"]].dropna()
        df_valores_clean["VALVALOR"] = pd.to_numeric(df_valores_clean["VALVALOR"])
        
        # Encontrar o maior valor do desemprego
        max_idx = df_valores_clean["VALVALOR"].idxmax()
        max_data = df_valores_clean.loc[max_idx, "VALDATA"]
        max_valor = df_valores_clean.loc[max_idx, "VALVALOR"]
        
        print(f"Maior taxa de desemprego: {max_data} - {max_valor:.2f}%")
