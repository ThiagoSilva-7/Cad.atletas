import streamlit as st
from paginas import cadastro, avaliacoes, objetivos, treinos, relatorios

st.set_page_config(page_title="App Corrida de Rua", layout="wide")
st.sidebar.title("Navegação")
pagina = st.sidebar.radio("Ir para:", [
    "Cadastro de Atletas",
    "Avaliações Físicas",
    "Definir Objetivos",
    "Planejamento de Treinos",
    "Relatórios de Desempenho"
])

if pagina == "Cadastro de Atletas":
    cadastro.pagina_cadastro()
elif pagina == "Avaliações Físicas":
    avaliacoes.pagina_avaliacoes()
elif pagina == "Definir Objetivos":
    objetivos.pagina_objetivos()
elif pagina == "Planejamento de Treinos":
    treinos.pagina_treinos()
elif pagina == "Relatórios de Desempenho":
    relatorios.pagina_relatarios()
