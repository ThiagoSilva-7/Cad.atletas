
import streamlit as st

def pagina_strava(atleta_id):
    st.header("🚴 Integração com Strava (Protótipo)")
    st.info("Esta seção simula o login com Strava e mostra como os dados seriam integrados futuramente.")
    if st.button("Simular login com Strava"):
        st.success("✅ Login com Strava simulado com sucesso!")
        st.write("Aqui apareceriam os treinos importados da conta Strava.")
