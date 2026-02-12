import streamlit as st
from openai import OpenAI
import time

# ================= CONFIGURAÇÃO VISUAL INICIAL =================
st.set_page_config(page_title="Gestor Ads Elite V6", page_icon="🦅", layout="wide")

# ================= SISTEMA DE LOGIN (NOVO) =================
if 'senha_correta' not in st.session_state:
    st.session_state.senha_correta = False

def tela_login():
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/9626/9626620.png", width=100)
        st.markdown("### 🔐 Área Restrita - Gestor Elite")
        senha_digitada = st.text_input("Digite a Senha de Acesso:", type="password")
        
        if st.button("Entrar no Sistema"):
            # ==========================================
            # 👇 TROQUE A SENHA AQUI (DENTRO DAS ASPAS)
            SENHA_MESTRA = "papai123" 
            # ==========================================
            
            if senha_digitada == SENHA_MESTRA:
                st.session_state.senha_correta = True
                st.success("✅ Acesso Liberado!")
                time.sleep(1)
                st.rerun()
            else:
                st.error("❌ Senha incorreta, Papai!")

# Se a senha não estiver correta, mostra o login e PARA O CÓDIGO (st.stop)
if not st.session_state.senha_correta:
    tela_login()
    st.stop()

# ==============================================================================
# DAQUI PARA BAIXO É O SEU SISTEMA (SÓ CARREGA SE TIVER LOGADO)
# ==============================================================================

# CSS para deixar com cara de Dashboard Profissional
st.markdown("""
<style>
    .main {background-color: #f8f9fa;}
    .stButton>button {width: 100%; border-radius: 5px; height: 50px; font-weight: bold;}
    
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        border-left: 5px solid #FF4B4B;
    }
    .card h3 {color: #333; font-size: 20px; margin-bottom: 10px;}
    
    .card-safe {border-left: 5px solid #00C851;}
    .card-danger {border-left: 5px solid #ff4444;}
    
    .big-title {font-size: 35px; font-weight: 800; color: #1E1E1E;}
    .subtitle {color: #777; font-size: 18px;}
</style>
""", unsafe_allow_html=True)

# ================= MEMÓRIA DO ROBÔ (SESSION STATE) =================
if 'resultado_estrategia' not in st.session_state:
    st.session_state['resultado_estrategia'] = None
if 'imagem_gerada' not in st.session_state:
    st.session_state['imagem_gerada'] = None

# ================= BARRA LATERAL =================
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/9626/9626620.png", width=80)
    st.title("🦅 Painel Elite V6")
    st.success("🔓 Usuário Logado")
    
    st.markdown("---")
    api_key = st.text_input("🔑 Cole sua API Key OpenAI:", type="password")
    st.caption("A chave é necessária para gerar o conteúdo.")
    
    st.markdown("---")
    st.markdown("### ⚙️ Configuração")
    nicho_black = st.checkbox("💀 Nicho Black (Anti-Ban)", value=False)
    
    if st.button("Sair / Logout"):
        st.session_state.senha_correta = False
        st.rerun()

# ================= TELA PRINCIPAL =================
st.markdown('<p class="big-title">Gestor Ads Pro V6.0</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Sistema com Memória de Sessão e Geração de Imagens.</p>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        nome_produto = st.text_input("📦 Nome do Produto", placeholder="Ex: Curso de Violão Online")
    with col2:
        url_site = st.text_input("🔗 URL Final", placeholder="Ex: www.violao.com")
    
    # Botão Principal (Gera o Texto)
    if st.button("🚀 1. GERAR ESTRATÉGIA DE TEXTO"):
        if not api_key:
            st.error("⚠️ Faltou a API Key na barra lateral!")
        elif not nome_produto:
            st.warning("⚠️ Digite o nome do produto!")
        else:
            client = OpenAI(api_key=api_key)
            modo = "BLINDADO (BLACK)" if nicho_black else "NORMAL"
            aviso_seguranca = "ATENÇÃO: Suavize promessas. Evite bloqueios." if nicho_black else ""

            prompt_sistema = f"""
            Você é um GESTOR DE TRÁFEGO EXPERT. Modo: {modo}. {aviso_seguranca}
            Gere uma resposta ESTRUTURADA em Markdown.
            Separe: Títulos, Descrições, Extensões, Palavras-Chave e Públicos.
            """
            prompt_usuario = f"""
            Produto: {nome_produto} / URL: {url_site}
            Crie a estratégia completa: Copy, Públicos, Negativas e Extensões.
            """

            with st.spinner("🦅 O Robô está escrevendo a estratégia..."):
                try:
                    response = client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=[{"role": "system", "content": prompt_sistema}, {"role": "user", "content": prompt_usuario}]
                    )
                    # SALVA NA MEMÓRIA DO STREAMLIT
                    st.session_state['resultado_estrategia'] = response.choices[0].message.content
                    st.success("✅ Estratégia de Texto Gerada e Salva na Memória!")
                except Exception as e:
                    st.error(f"Erro no GPT: {e}")
    st.markdown('</div>', unsafe_allow_html=True)

# ================= EXIBIÇÃO DOS RESULTADOS (SE HOUVER NA MEMÓRIA) =================
if st.session_state['resultado_estrategia']:
    resultado = st.session_state['resultado_estrategia']
    
    tab_estrat, tab_copy, tab_img = st.tabs(["📊 Estratégia & Público", "📝 Copy Pronta", "🎨 Gerador de Imagem (DALL-E)"])
    
    # --- ABA 1: ESTRATÉGIA ---
    with tab_estrat:
        st.markdown(resultado) # Mostra o texto bruto

    # --- ABA 2: COPY ---
    with tab_copy:
        st.text_area("Copie os textos aqui:", value=resultado, height=500)
        
    # --- ABA 3: IMAGEM (AGORA FUNCIONA!) ---
    with tab_img:
        st.markdown("""
        <div class="card">
            <h3>🎨 Criativo Visual</h3>
            <p>Clique abaixo para gerar uma imagem exclusiva para este produto. Custa alguns centavos.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Botão da Imagem (Independente)
        if st.button("📸 2. GERAR IMAGEM AGORA ($)"):
            if not api_key or not nome_produto:
                 st.error("Precisa da API Key e do Nome do Produto.")
            else:
                client = OpenAI(api_key=api_key)
                with st.spinner("Pintando a imagem no DALL-E 3..."):
                    try:
                        prompt_img = f"Professional high quality advertising image for {nome_produto}. Modern digital marketing style, catchy visual, no text over image."
                        res_img = client.images.generate(
                            model="dall-e-3",
                            prompt=prompt_img,
                            size="1024x1024",
                            quality="standard",
                            n=1,
                        )
                        # Salva a URL da imagem na memória também
                        st.session_state['imagem_gerada'] = res_img.data[0].url
                    except Exception as e:
                        st.error(f"Erro ao gerar imagem (Verifique saldo/API): {e}")

        # Se tiver imagem na memória, mostra ela
        if st.session_state['imagem_gerada']:
             st.image(st.session_state['imagem_gerada'], caption="Imagem Gerada pela IA")
             st.markdown(f"[📥 Baixar Imagem em Alta Resolução]({st.session_state['imagem_gerada']})")

# ================= RODAPÉ =================
st.markdown("---")
st.markdown("<center>🦅 Sistema V6.0 (Blindado com Senha) - Desenvolvido por Papai</center>", unsafe_allow_html=True)