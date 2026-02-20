# -*- coding: utf-8 -*-
import streamlit as st
from openai import OpenAI

# ================= CONFIGURAÇÃO DA PÁGINA =================
st.set_page_config(page_title="Gestor Ads Pro Elite", page_icon="🚀", layout="wide")

# ================= 🛡️ ESCUDO ANTI-TRADUTOR (BLINDA O SITE CONTRA ERROS DO CHROME) =================
st.markdown("""
    <meta name="google" content="notranslate">
    <style>
        /* Bloqueia a ação do tradutor automático que quebra os botões do sistema */
        .skiptranslate { display: none !important; }
        body { top: 0px !important; }
    </style>
""", unsafe_allow_html=True)

# ================= 📋 BANCO DE DADOS DO PAPAI =================
CLIENTES_AUTORIZADOS = {
    "PAPAI-ADMIN-001": "Dono do Sistema",
    "TESTE-GRATIS-123": "Cliente Teste",
    "CLIENTE-VIP-777": "João do Tráfego"
}

# ================= 🔐 SISTEMA DE LOGIN (A CATRACA) =================
if "autenticado" not in st.session_state:
    st.session_state.autenticado = False

if not st.session_state.autenticado:
    st.title("🔒 Acesso Restrito - Gestor Ads Elite")
    st.markdown("Bem-vindo! Digite sua **Chave VIP** para acessar a máquina de tráfego.")
    
    chave_digitada = st.text_input("🔑 Chave de Acesso:", type="password", placeholder="Ex: CLIENTE-VIP-777")
    
    if st.button("Entrar no Sistema", type="primary"):
        chave_limpa = chave_digitada.strip()
        
        if chave_limpa in CLIENTES_AUTORIZADOS:
            st.session_state.autenticado = True
            st.session_state.nome_cliente = CLIENTES_AUTORIZADOS[chave_limpa]
            st.rerun() 
        else:
            st.error("❌ Chave inválida ou expirada. Fale com o suporte.")
            
    st.markdown("---")
    st.caption("Quer ter acesso? Compre sua licença agora mesmo.")
    st.stop()

# ================= 🚀 O ROBÔ LIBERADO =================
with st.sidebar:
    st.success(f"👤 Bem-vindo, **{st.session_state.nome_cliente}**!")
    if st.button("Sair (Logout)"):
        st.session_state.autenticado = False
        st.rerun()
    st.markdown("---")
    st.info("🟢 Sistema Conectado e Blindado. Motor IA 100% Operacional.")

st.title("🚀 Máquina de Campanhas e Tráfego Pago")
st.markdown("""
**Transforme seu produto em uma campanha pronta em segundos.**
*Copywriter + Gestor de Tráfego: Textos milimétricos e configurações exatas.*
""")

# ================= 🔑 A MÁGICA: PUXANDO A CHAVE DO COFRE INVISÍVEL =================
try:
    api_key = st.secrets["OPENAI_API_KEY"]
except:
    st.error("🚨 ERRO DO SISTEMA: A chave da OpenAI não foi encontrada no Cofre do Streamlit! Papai, vá nas configurações do site e adicione a chave.")
    st.stop()

# ================= FORMULÁRIO DO USUÁRIO =================
with st.form("form_ads"):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        plataforma = st.selectbox("Qual a Plataforma?", ["Google Ads (Pesquisa)", "Facebook Ads / Instagram", "TikTok Ads"])
    with col2:
        tipo_nicho = st.selectbox("Nível de Risco (Políticas)", ["Nicho White (Seguro)", "Nicho Black (Risco de Bloqueio)"])
    with col3:
        nome_produto = st.text_input("Nome do Produto/Serviço", placeholder="Ex: Robô V21 Forex")
        
    col4, col5 = st.columns(2)
    with col4:
        url_site = st.text_input("Site (URL)", placeholder="Ex: www.robov21.com.br")
        publico_alvo = st.text_input("Público Alvo (Quem compra?)", placeholder="Ex: Investidores iniciantes que querem renda extra")
    with col5:
        beneficios = st.text_area("Principais Benefícios (Ouro)", placeholder="Ex: Automático, Risco Baixo, Instalação Fácil...", height=110)
    
    submit_btn = st.form_submit_button("🔥 GERAR CAMPANHA COMPLETA AGORA", use_container_width=True)

# ================= A MÁGICA (INTELIGÊNCIA ARTIFICIAL) =================
if submit_btn:
    if not nome_produto or not beneficios:
        st.warning("⚠️ Preencha pelo menos o Nome e os Benefícios!")
    else:
        try:
            client = OpenAI(api_key=api_key)
            
            regra_black = ""
            if "Black" in tipo_nicho:
                regra_black = """
                ALERTA DE NICHO BLACK:
                - Rigor maximo com as politicas da plataforma.
                - PROIBIDO usar palavras que dao bloqueio ("rapido", "garantido", "dinheiro facil", "cura", "perder peso").
                - Trabalhe com curiosidade e metaforas. Zero claims exagerados.
                """
            else:
                regra_black = "- Nicho White: Foque nos beneficios diretos e transformacao clara."

            regras_textos = ""
            estrutura_trafego = ""
            
            if "Google" in plataforma:
                regras_textos = """
                1. 15 Titulos (MAXIMO 30 CARACTERES cada).
                2. 4 Descricoes (MAXIMO 90 CARACTERES cada).
                3. 6 Sitelinks curtos (MAXIMO 25 CARACTERES cada).
                4. 4 Frases de Destaque / Snippets Estruturados.
                """
                estrutura_trafego = """
                =========================================
                🎯 2. CONFIGURACAO DA CAMPANHA (O MAPA DA MINA - GOOGLE ADS)
                =========================================
                - Objetivo da Campanha: VENDAS
                - Palavras-chave Positivas: (10 termos quentes)
                - Palavras-chave Negativas: (10 termos cruciais)
                - Publico-Alvo Demografico: (Renda, Idade e Genero)
                - Dispositivos: (Focar em Celular, Computador ou ambos)
                - Estrategia de Lance Recomendada: Maximizar Conversoes
                """
            elif "Facebook" in plataforma:
                regras_textos = """
                1. Headline do Anuncio (Titulo Curto).
                2. Copy Principal Persuasiva (Texto longo para o corpo do anuncio).
                """
                estrutura_trafego = """
                =========================================
                🎯 2. CONFIGURACAO DA CAMPANHA (O MAPA DA MINA - FACEBOOK ADS)
                =========================================
                NIVEL 1: CAMPANHA
                - Tipo de Compra: Leilao
                - Objetivo da Campanha: Vendas
                - Orcamento de Campanha Advantage+ (CBO): Ativado
                - Estrategia de Orcamento: Volume mais alto
                - Orcamento Diario Sugerido: R$ 25,00
                
                NIVEL 2: CONJUNTO DE ANUNCIOS
                - Meta de Desempenho: Maximizar numero de conversoes
                - Pixel / Evento: Iniciar Finalizacao de Compra (Initiate Checkout)
                - Publico Advantage+: Ativado
                - Localizacao: Inclusao - Brasil
                - Segmentacao: (Sugira interesses e exclusoes)
                - Posicionamentos: Advantage+ Ativado
                
                NIVEL 3: ANUNCIO
                - Nome do Anuncio: (Crie um nome focado no angulo)
                - Rastreamento: Eventos do Site Ativados
                - Parametros de URL (UTM): (Crie o link com utm_source e utm_medium)
                """
            else: 
                regras_textos = "Ganchos (Hooks) para os 3 primeiros segundos de video e Texto curto para a legenda."
                estrutura_trafego = "Objetivo (Sempre focado em Conversoes/Vendas), Interesses e Comportamentos ideais no TikTok Ads."

            prompt_sistema = f"""
            Voce e um Especialista Senior em Trafego Pago e Copywriting.
            Sua missao e preencher as configuracoes tecnicas e escrever copys matadoras focadas em conversao.
            
            REGRAS DE OURO PARA TEXTOS:
            - Respeite rigorosamente as limitacoes de caracteres quando for Google Ads.
            - NAO use aspas nas respostas.
            
            {regra_black}
            """
            
            prompt_usuario = f"""
            Crie a estrutura da campanha para:
            Plataforma: {plataforma}
            Nicho: {tipo_nicho}
            Produto: {nome_produto}
            URL: {url_site}
            Publico: {publico_alvo}
            Beneficios: {beneficios}
            
            SAIDA OBRIGATORIA NESTE FORMATO EXATO:
            
            =========================================
            📝 1. TEXTOS DO ANUNCIO (COPY)
            =========================================
            {regras_textos}
            
            {estrutura_trafego}
            
            =========================================
            👥 3. ANALISE DO PUBLICO E ANGULO
            =========================================
            - Qual a principal dor desse publico?
            - Qual a objecao principal a ser quebrada na pagina de vendas?
            """

            with st.spinner(f"🤖 O Cérebro Tubarão está montando a estrutura de {plataforma}..."):
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": prompt_sistema},
                        {"role": "user", "content": prompt_usuario}
                    ],
                    temperature=0.7
                )
                
                resultado = response.choices[0].message.content
                
                st.success(f"✅ Guia Completo para {plataforma} Gerado com Sucesso!")
                st.text_area("Copie sua Estrutura Completa Aqui:", value=resultado, height=650)
                
        except Exception as e:
            st.error(f"Erro na conexão com a IA. Detalhes: {e}")

# ================= RODAPÉ =================
st.markdown("---")
st.caption("Desenvolvido por Papai & Parceiro Ltda. 🦅")
