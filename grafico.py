import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#DATASET utilizado com os dados sem filtro
st.subheader("DATASET utilizado!")
dados=pd.read_csv("top.csv",encoding="UTF-8",sep=",",lineterminator='\n',index_col=0)
st.write(dados)
#Filtrando o DATASET com algumas colunas#
dados=pd.read_csv("top.csv",encoding="UTF-8",sep=",",lineterminator='\n',usecols=["Nome_do_Filme","Renda_Total","Orçamento"])
#tirando nas linhas que tem campo vazio
dados=dados.dropna().reset_index(drop=True)
#ordenando o DATASET de acordo com a renda dos filmes
dados=dados.sort_values(by="Renda_Total",ascending=False).reset_index(drop=True)
#construção do grafico no estilo st.bar_chart
st.subheader("Gráficos das maiores Bilheterias e seus orçamentos!")
st.bar_chart(data=dados.head(10),x="Nome_do_Filme", y=["Orçamento","Renda_Total"],width=900, height=500,use_container_width=True)