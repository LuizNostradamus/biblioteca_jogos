import streamlit as st
import banco

st.title("Bilioteca de jogos")
st.write("Cadastro de jogo")

with st.form("cadastro", clear_on_submit=True):
    titulo = st.text_input("Nome do produto")
    plataforma = st.selectbox("plataforma", ["PS5", "Xbox", "Switch", "PC", "Mobile"])
    genero = st.selectbox("Genero", [
    "Ação",
    "Aventura",
    "RPG",
    "FPS",
    "Battle Royale",
    "MOBA",
    "Estratégia",
    "Simulação",
    "Esporte",
    "Corrida",
    "Luta",
    "Plataforma",
    "Terror",
    "Puzzle",
    "Mundo aberto",
    "Roguelike",
    "Indie",
    "Outro",
])
    status_jogo = st.selectbox("Status", ["Jogando", "Terminado", "Abandonado"])
    nota = st.number_input("Nota", min_value=0.0,step=0.50, max_value=10.0)
    preco = st.number_input("Preço R$", min_value=0.0,step=10.0)
    enviar = st.form_submit_button("Cadastrar")

# Verificar erro
if enviar:
    if titulo == "" or genero == "" or plataforma == "" or status_jogo == "" or nota == "" or preco == "":
        st.warning("Informação invalida")
    else:
        banco.cadastrar(titulo, plataforma, genero, status_jogo, nota, preco)
        st.success("Cadastrado")