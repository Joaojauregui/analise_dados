import pandas as pd

df = pd.read_csv(r'c:\Users\202502643535\Documents\ANALISE DE DADOS\titanic.csv')

# Questão 2: Filtrar passageiros do sexo feminino
df_females = df[df['Sex'] == 'female']

# Questão 3: Contar sobreviventes
total_survivors = df['Survived'].sum()

# Questão 4: Quantos Homens Sobreviveram?
men_survived = df[(df['Sex'] == 'male') & (df['Survived'] == 1)].shape[0]

# Questão 5: Calcular quantos passageiros tem o nome "John"
john_count = df[df['Name'].str.contains('John', case=False)].shape[0]
