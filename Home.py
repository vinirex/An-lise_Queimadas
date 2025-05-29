from matplotlib import pyplot as plt
import streamlit as st
import pandas as pd
import numpy as np
import scipy.stats as stats
import seaborn as sns
from streamlit_extras.app_logo import add_logo


# Configuração da página
st.set_page_config(page_title="Queimadas", layout="wide")

# Sessão de Colaboradores
st.sidebar.title("Colaboradores 🤝")
colaboradores = [
    {"nome": "Vinicius Silva - RM553240"},
    {"nome": "Victor Didoff - RM552965"},
    {"nome": "Matheu Zottis - RM94119"},
]

for colaborador in colaboradores:
    st.sidebar.write(colaborador["nome"])

# Carregar os dados
file_path = "wildfires.csv"  # Substitua pelo caminho real do arquivo
df = pd.read_csv(file_path)

np.random.seed(14)

# Seleciona 500 mil quemadas aleatórias
amostra = df.sample(n=500_000, replace=False, random_state=14)

st.title("Análise de Queimadas 🔥")


# Mapeando as classes de fogo para cores
fire_classes = amostra['FIRE_SIZE_CLASS'].unique()
palette = sns.color_palette("rocket", len(fire_classes))
color_map = dict(zip(fire_classes, palette))

# Plotando os pontos no plano latitude x longitude
fig, ax = plt.subplots(figsize=(10, 6))
for fire_class in fire_classes:
    subset = amostra[amostra['FIRE_SIZE_CLASS'] == fire_class]
    ax.scatter(subset['LONGITUDE'], subset['LATITUDE'], 
               label=fire_class, 
               color=color_map[fire_class], 
               alpha=0.5, s=5)

ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_title('Distribuição das Queimadas por Classe')
ax.legend(title='FIRE_CLASS', bbox_to_anchor=(1.05, 1), loc='upper left')
st.pyplot(fig)

# Gráfico de incêndios por ano
st.subheader("Quantidade de Incêndios por Ano")
incendios_por_ano = amostra['FIRE_YEAR'].value_counts().sort_index()
fig_ano, ax_ano = plt.subplots(figsize=(10, 4))
sns.barplot(x=incendios_por_ano.index, y=incendios_por_ano.values, ax=ax_ano, palette="rocket")
ax_ano.set_xlabel("Ano")
ax_ano.set_ylabel("Quantidade de Incêndios")
ax_ano.set_title("Incêndios por Ano")
plt.xticks(rotation=45)
st.pyplot(fig_ano)

# Gráfico comparando NWCG_GENERAL_CAUSE dos incêndios
st.subheader("Comparação das Causas Gerais dos Incêndios")
causas = amostra['NWCG_GENERAL_CAUSE'].value_counts()
fig_causa, ax_causa = plt.subplots(figsize=(10, 4))
sns.barplot(x=causas.index, y=causas.values, ax=ax_causa, palette="viridis")
ax_causa.set_xlabel("Causa Geral")
ax_causa.set_ylabel("Quantidade de Incêndios")
ax_causa.set_title("Distribuição das Causas Gerais dos Incêndios")
plt.xticks(rotation=45, ha='right')
st.pyplot(fig_causa)

# Gráfico de classificação das causas dos incêndios
st.subheader("Classificação das Causas dos Incêndios")
classificacao_causas = amostra['NWCG_CAUSE_CLASSIFICATION'].value_counts()
fig_classificacao, ax_classificacao = plt.subplots(figsize=(8, 4))
sns.barplot(x=classificacao_causas.index, y=classificacao_causas.values, ax=ax_classificacao, palette="rocket")
ax_classificacao.set_xlabel("Classificação da Causa")
ax_classificacao.set_ylabel("Quantidade de Incêndios")
ax_classificacao.set_title("Distribuição das Classificações das Causas dos Incêndios")
plt.xticks(rotation=45, ha='right')
st.pyplot(fig_classificacao)