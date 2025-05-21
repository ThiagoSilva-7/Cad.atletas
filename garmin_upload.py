
import streamlit as st

def pagina_garmin_upload(atleta_id):
    st.header("📤 Upload de arquivos Garmin (.tcx ou .fit)")
    uploaded_file = st.file_uploader("Enviar arquivo TCX ou FIT", type=["tcx", "fit"])
    if uploaded_file:
        st.success(f"Arquivo '{uploaded_file.name}' enviado com sucesso!")
        st.write("Esta funcionalidade será estendida para leitura e importação dos dados do arquivo.")
