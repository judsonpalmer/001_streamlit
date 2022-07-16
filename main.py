import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

dados = pd.read_csv('alura1.csv')

def mostra_linha(df):
    quant_linha = st.sidebar.slider('Selecione o número de linhas: ')
    st.write(df.head(quant_linha).style.format(subset=['Valor'], formatter='{:.2f}'))


def plot_estoque(dataframe, categoria):
    dados_plot = dataframe.query('Categoria == @categoria')
    fig, ax = plt.subplots(figsize=(10, 3))
    ax = sns.barplot(x='Produto', y='Quantidade', data=dados_plot)
    ax.set_title(f'Quantidade em estoque dos produtos de {categoria}', fontsize=12)
    ax.set_xlabel('Produtos (x)', fontsize=6)
    ax.tick_params(rotation=0, axis='x')
    ax.set_ylabel('Quantidade (y)', fontsize=6)
    return fig


st.title('Eletrônicos: Supermercado Palmer\n')
st.write('Iremos validar estudos sobre os produtos de eletrônicos')

# filtros
checkbox = st.sidebar.checkbox('Mostrar tabela')
if checkbox:
    st.sidebar.markdown('## Filtro para tabela')
    categorias = list(dados['Categoria'].unique())
    categorias.append('Todas')
    categoria = st.sidebar.selectbox('Selecione a categoria para apresentar a tabela', options=categorias)
    if categoria != 'Todas':
        df_categoria = dados.query('Categoria == @categoria')
        mostra_linha(df_categoria)
    else:
        mostra_linha(dados)

#filtros para gráfico

st.sidebar.markdown('## Filtro para gráfico')
catgfx = st.sidebar.selectbox('Selecione categoria para gráfico: ', options=dados['Categoria'].unique())
figura = plot_estoque(dados, catgfx)
st.pyplot(figura)
