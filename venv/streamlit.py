import streamlit as st
import pandas as pd
import plotly.express as px
st.title('Top 10.000 TMDb movies data - exploratory analysis')
st.subheader("*Quantidades de Filmes Com uma Determinada Duração*")
filmesdf = pd.read_csv('tmdb.csv', lineterminator='\n', index_col=0)
tempo = filmesdf['runtime']

# Sidebar para selecionar a faixa de duração
duracao_min = int(tempo.min())
duracao_max = int(tempo.max())
selecionar_tempo = st.sidebar.slider('*Selecione a duração do filme*', duracao_min, duracao_max, (duracao_min, duracao_max))

# Filtra os dados com base na faixa de duração selecionada
filtrar_info = filmesdf[(filmesdf['runtime'] >= selecionar_tempo[0]) & (filmesdf['runtime'] <= selecionar_tempo[1])]

# Cria o gráfico
grafico = px.histogram(filtrar_info, x='runtime', nbins=20,
                       labels={'x': 'Tempo de duração', 'y': 'Quantidade de filmes'})

grafico.update_layout(
    xaxis_title='Tempo de duração',
    yaxis_title='Quantidade de filmes'
)

# Exibe o gráfico
st.plotly_chart(grafico)
