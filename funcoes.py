# manipulação de dados em tabelas
import pandas as pd
# Operações matemáticas e arrays
import numpy as np
# Formatar os eixos
from matplotlib.ticker import FuncFormatter
import random
from datetime import datetime, timedelta

# Função que gera dados fictícios de vendas
def gerador_dados_ficticios(num_registros = 1000):

    print(f"\nIniciando a geração de {num_registros} registros de vendas...")

    produtos = {
        'Laptop Gamer': {'categoria':'Eletrônicos', 'preco': 7500.00},
        'Mouse Vertical': {'categoria':'Acessórios', 'preco': 250.00},
        'Teclado Mecânico': {'categoria':'Acessórios', 'preco': 550.00},
        'Monitor Ultrawide': {'categoria':'Eletrônicos', 'preco': 2800.00},
        'Cadeira Gamer': {'categoria':'Móveis', 'preco': 1200.00},
        'Headset 7.1': {'categoria':'Acessórios', 'preco': 800.00},
        'Placa de Vídeo': {'categoria':'Hardware', 'preco': 4500},
        'SSD 1TB': {'categoria':'Hardware', 'preco': 600}
    }

    # lista apenas com os nomes dos produtos
    lista_produtos = list(produtos.keys())

    cidades_estados = {
        'São Paulo':'SP', 'Rio de Janeiro':'RJ', 'Belo Horizonte':'MG',
        'Porto Alegre':'RS', 'Salvador':'BH', 'Curitiba':'PR',
        'Fortaleza':'CE'
    }

    #lista apenas com os nomes das cidades
    lista_cidades = list(cidades_estados.keys())

    #lista que armazenará dos registros de vendas
    dados_vendas = []

    #data inicial dos pedidos
    data_inicial = datetime(2026, 1, 1)

    #Loop para gerar registros de vendas
    for i in range(num_registros):

        #selecionar um produto
        produto_nome = random.choice(lista_produtos)

        #selecionar uma cidade
        cidade = random.choice(lista_cidades)

        #quantidade de produtos vendidos(1 a 7)
        quantidade = np.random.randint(1,8)

        #caldula a data do pedido a partir da data inicial
        data_pedido = data_inicial + timedelta(days = int(i/5), hours = random.randint(0, 23))

        #aplicar desconto aos mouses e teclados de até 10%
        if produto_nome in ['Mouse Vertical', 'Teclado Mecânico']:
            preco_unitario = produtos[produto_nome]['preco'] * np.random.uniform(0.9,1.0)
        else:
            preco_unitario = produtos[produto_nome]['preco']

        #adiciona um registro de vendas na lista
        dados_vendas.append({
            'ID_Pedido': 1000 + i,
            'Data_Pedido': data_pedido,
            'Nome_Produto': produto_nome,
            'Categoria': produtos[produto_nome]['categoria'],
            'Preco_Unitario': round(preco_unitario, 2),
            'Quantidade': quantidade,
            'ID_Cliente': np.random.randint(100,150),
            'Cidade': cidade,
            'Estado': cidades_estados[cidade]
        })
    print('Geração de dados concluída.\n')

    #retorna os dados no formato DataFrame
    return pd.DataFrame(dados_vendas)


def formatador(y, pos):

    if y >= 1_000_000:

        return f'R$ {y/1000000:,.1f}M'

    else:

        return f'R$ {y/1000:,.0f}K'
