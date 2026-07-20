import streamlit as st

# Configuração da página
st.set_page_config(page_title="Meu Cartão", page_icon="💗", layout="centered")

# Título e Foto / Banner
st.title("Olá! Eu sou a Yas")
st.image("https://www.sciencefriday.com/segments/jwst-discoveries-galaxy-formation/", width=150) # Suba sua foto ou link de imagem

st.subheader("Estudante de engenharia da computação")
st.write("Conecte-se comigo ou mande uma mensagem abaixo:")

# Botões de Redes Sociais
col1, col2 = st.columns(2)
with col1:
    st.link_button("📂 Meu GitHub", "https://github.com/yasmimtaveira")
with col2:
    st.link_button("💼 LinkedIn", "www.linkedin.com/in/yasmim-taveira-lopes-40a9b335b")

st.divider()

# Exemplo de Interatividade: Formulário de Mensagem / RSVP
with st.form("contato"):
    nome = st.text_input("Seu nome: ")
    mensagem = st.text_area("Sua mensagem: ")
    enviar = st.form_submit_button("Enviar Mensagem")
    
    if enviar:
        st.success(f"Obrigado, {nome}! Sua mensagem foi recebida.")