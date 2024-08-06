import pandas as pd

# Criação de um DataFrame simples
data = {
    'Nome': ['Ana', 'Bruno', 'Carlos'],
    'Idade': [23, 30, 25],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']
}

df = pd.DataFrame(data)

# Exibindo o DataFrame
print("DataFrame Original:")
print(df)

# Selecionando uma coluna
nomes = df['Nome']
print("\nNomes:")
print(nomes)

# Filtrando dados (pessoas com idade maior que 25)
df_filtrado = df[df['Idade'] > 25]
print("\nPessoas com idade maior que 25:")
print(df_filtrado)

# Adicionando uma nova coluna
df['Profissão'] = ['Engenheira', 'Médico', 'Professor']
print("\nDataFrame com Nova Coluna:")
print(df)

# Calculando a média das idades
media_idade = df['Idade'].mean()
print("\nMédia das Idades:")
print(media_idade)
