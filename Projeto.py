# manipulação de dados em tabelas
from hmac import digest_size

import pandas as pd
# Geração de gráficos
import matplotlib.pyplot as plt
# Visualização estatística de dados
import seaborn as sns
# Formatar os eixos
from matplotlib.ticker import FuncFormatter
from funcoes import gerador_dados_ficticios, formatador

df_vendas = gerador_dados_ficticios(500)
type(df_vendas)
print(
#linhas x colunas
df_vendas.shape,

#5 primeiras linhas do DataFrame
df_vendas.head(),

#5 ultimas linhas do DataFrame
df_vendas.tail(),

#informações gerais sobre o DataFrame
df_vendas.info(),

#resumo estatístico
df_vendas.describe(),

#tipos de dados
df_vendas.dtypes
)

df_vendas['Data_Pedido'] = pd.to_datetime(df_vendas['Data_Pedido'])

#coluna de faturamento(preço*quantidade)
df_vendas['Faturamento'] = df_vendas['Preco_Unitario'] * df_vendas['Quantidade']

#coluna de status de entrega
df_vendas['Status_Entrega'] = df_vendas['Estado'].apply(lambda estado: 'Rápida' if estado in ['SP','RJ','MG'] else 'Normal')

print(
df_vendas.info(),
df_vendas.head()
)

#cria o objeto formatador
formatter = FuncFormatter(formatador)

#TOP 10 PRODUTOS MAIS VENDIDOS

#soma a quantidade e ordena para encontrar os mais vendidos
top_10_produtos = df_vendas.groupby('Nome_Produto')['Quantidade'].sum().sort_values(ascending = False).head(10)

print(top_10_produtos)

#define um estilo para os gráficos
sns.set_style("whitegrid")


#cria a figura com tamanho 12x7
plt.subplots(figsize = (12, 7))

#cria o grafico de barras horizontais
top_10_produtos.sort_values(ascending = True).plot(kind = 'barh', color = 'skyblue')

#adiciona títulos e tabélas
plt.title('Top 10 Produtos Mais Vendidos', fontsize = 16)
plt.xlabel('Quantidade Vendida', fontsize = 12)
plt.ylabel('Produto', fontsize = 12)

#

#FATURAMENTO MENSAL

#Cria uma coluna 'Mes'
df_vendas['Mes'] = df_vendas['Data_Pedido'].dt.to_period('M')

#agrupa o mes e soma o faturamento
faturamento_mensal = df_vendas.groupby('Mes')['Faturamento'].sum().sort_values(ascending = False)

#converte o índice para a string
faturamento_mensal.index = faturamento_mensal.index.strftime('%Y-%m')

faturamento_mensal.map('R$ {:,.2f}'.format)

#cria figura com tamanho 12x6
fig, ax = plt.subplots(figsize = (12, 7))

#aplica o formatador ao eixo y
ax.yaxis.set_major_formatter(formatter)

#plota os dados de faturamento mensal em formato de linha
faturamento_mensal.plot(kind = 'line',
                        marker = 'o',
                        linestyle = '-',
                        color = 'green',
                        )

#títulos e tabélas do gráfico
plt.title('Evolução do Faturamento Mensal', fontsize = 16)
plt.xlabel('Mes', fontsize = 12)
plt.ylabel('Faturamento (R$)', fontsize = 12)

#rotaciona os valores do eixo x
(plt.xticks(rotation = 45))

#adiciona grade personalizada
plt.grid(True, which = 'both', linestyle = 'solid', linewidth = 0.5)

#

#VENDAS POR ESTADO
#formula semelhante as anteriores

vendas_estado = df_vendas.groupby(f'Estado')['Faturamento'].sum().sort_values(ascending = False)

vendas_estado.map('R$ {:,.2f}'.format)

#cria a figura e os eixos
fig, ax = plt.subplots(figsize = (12, 7))

#aplica o formatador ao eixo y
ax.yaxis.set_major_formatter(formatter)

vendas_estado.plot(kind = 'bar', color = sns.color_palette('husl', 7))

plt.title('Faturamento Por Estado', fontsize = 16)
plt.xlabel('Estado', fontsize = 12)
plt.ylabel('Faturamento (R$)', fontsize = 12)
plt.xticks(rotation = 0)

#

#Faturamento por categoria

#Agrupa por categoria, soma o faturamento e formata como moeda
faturamento_categoria = df_vendas.groupby('Categoria')['Faturamento'].sum().sort_values(ascending = False)

faturamento_categoria.map('R$ {:,.2f}'.format)

#ordena os dados
faturamento_ordenado = faturamento_categoria.sort_values(ascending = False)

#cria a figura e os eixos
fig, ax = plt.subplots(figsize = (12, 7))

#aplica o formatador ao eixo y
ax.yaxis.set_major_formatter(formatter)

#plota os dados usando o objeto 'ax'
faturamento_ordenado.plot(kind = 'bar', ax = ax, color = sns.color_palette('viridis', len(faturamento_ordenado)))

#adiciona títulos e labels usando 'ax.set...'
ax.set_title('Faturamento por Categoria', fontsize = 16)
ax.set_xlabel('Categoria', fontsize = 12)
ax.set_ylabel('Faturamento', fontsize = 12)

plt.xticks(rotation = 45, ha = 'right')
plt.tight_layout()
plt.show()




