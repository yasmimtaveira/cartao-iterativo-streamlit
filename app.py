import streamlit as st

# Configuração da página
st.set_page_config(page_title="Meu Cartão", page_icon="💗", layout="centered")

# Título e Foto / Banner
st.title("presentinho pro melhor namorado do mundo!!")

p1, p2, p3 = st.columns(3)

with p2:
    st.image("snoopy.jpg", width=300) # Suba sua foto ou link de imagem

st.subheader("José, eu amo você!")
st.write("Ainda não consigo fazer o presente que você merece, mas espero que ache esse fofo 💘")

# Botões de Redes Sociais
col1, col2, col3 = st.columns(3)
with col1:
    st.link_button("🎼 Uma música!", "https://youtu.be/P-wyIzdAnvc?si=qUJrmFUjXehOlc0j")
with col2:
    st.link_button("💞 A gente <3", "https://www.instagram.com/stories/highlights/17978243759574763/?hl=en")
with col3:
    st.image("beijo.png", width= 100)

st.divider()

# Exemplo de Interatividade: Formulário de Mensagem / RSVP
st.write("Dê uma nota para essa declaração:")
with st.form("Dê uma nota para essa declaração:"):
    nome = st.text_input("Seu nome: ")
    mensagem = st.text_area("Sua mensagem: ")
    enviar = st.form_submit_button("Enviar 😽")
    
    if enviar:
        st.success(f"Obrigada, Amor! Sua mensagem foi enviada.")
