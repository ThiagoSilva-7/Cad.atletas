
import streamlit as st
from paginas import avaliacoes, objetivos, treinos, analises
from strava_integration import pagina_strava
from garmin_upload import pagina_garmin_upload

st.set_page_config(page_title="Cadastro de Atletas", layout="wide")

st.sidebar.title("📂 Navegação")
pagina = st.sidebar.radio("Ir para", ["Avaliações", "Objetivos", "Treinos", "Análises", "Strava", "Garmin"])

# Simulando seleção de atleta
atleta_id = 1  # Substituir por autenticação ou seleção real

if pagina == "Avaliações":
    avaliacoes.pagina_avaliacoes(atleta_id)
elif pagina == "Objetivos":
    objetivos.pagina_objetivos(atleta_id)
elif pagina == "Treinos":
    treinos.pagina_treinos(atleta_id)
elif pagina == "Análises":
    analises.pagina_analises(atleta_id)
elif pagina == "Strava":
    pagina_strava(atleta_id)
elif pagina == "Garmin":
    pagina_garmin_upload(atleta_id)
