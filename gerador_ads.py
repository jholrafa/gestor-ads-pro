import streamlit as st
from openai import OpenAI

# ================= CONFIGURAÇÃO DA PÁGINA =================
st.set_page_config(page_title="Gestor Ads Pro Elite", page_icon="🚀", layout="wide")

# Título e Subtítulo
st.title("🚀 Máquina de Campanhas e Tráfego Pago")
st.markdown("""
**Transforme seu produto em uma campanha pronta em segundos.**
*Copywriter + Gestor de Tráfego: Textos milimétricos e configurações exatas (Públicos, Dispositivos e Estratégia).*
""")

# ================= BARRA LATERAL (CONFIGURAÇÃO) =================
with st.sidebar:
    st.header("🔑 Configuração")
    api_key = st.text_input("Cole sua API Key da OpenAI aqui:", type="password")
    st.markdown("---")
    st.info("💡 Dica: Para vender isso, você esconderia essa chave e cobraria assinatura do cliente.")

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
    
    # Botão de Ação
    submit_btn = st.form_submit_button("🔥 GERAR CAMPANHA COMPLETA AGORA", use_container_width=True)

# ================= A MÁGICA (INTELIGÊNCIA ARTIFICIAL) =================
if submit_btn:
    if not api_key:
        st.error("⚠️ Você precisa colocar a API Key da OpenAI na barra lateral para funcionar!")
    elif not nome_produto or not beneficios:
        st.warning("⚠️ Preencha pelo menos o Nome e os Benefícios!")
    else:
        client = OpenAI(api_key=api_key)
        
        # INSTRUÇÕES DE CONTINGÊNCIA (NICHO BLACK)
        regra_black = ""
        if tipo_nicho == "Nicho Black (Risco de Bloqueio)":
            regra_black = """
            🚨 ALERTA DE NICHO BLACK (CONTINGÊNCIA ATIVADA):
            - O rigor com as políticas da plataforma é MÁXIMO.
            - PROIBIDO usar palavras que dão ban/bloqueio (ex: "rápido", "garantido", "dinheiro fácil", "cura", "perder peso", "fique rico").
            - Use COPY BLINDADA: Trabalhe com curiosidade, metáforas, e foque no "mecanismo único" ao invés da promessa agressiva.
            - O texto precisa passar pela aprovação automática do robô da plataforma sem levantar suspeitas (zero claims exagerados).
            """
        else:
            regra_black = "- Nicho White: Foque nos benefícios diretos e transformação clara, mantendo as boas práticas da plataforma."

        # O PROMPT DE ENGENHARIA (O Segredo do App)
        prompt_sistema = f"""
        Você é um Especialista Sênior em Tráfego Pago e Copywriting (Nível Gestor Elite).
        Sua missão é criar a estrutura de textos de alta conversão E o passo a passo de configuração da campanha na plataforma escolhida.
        
        REGRAS DE OURO PARA TEXTOS:
        - Se for Google Ads: Títulos MÁXIMO 30 CARACTERES. Descrições MÁXIMO 90 CARACTERES. Sitelinks Max 25 caracteres. (Conte cada letra e espaço. Se passar, você falha).
        - Se for Facebook/Insta: Crie a Copy Principal (Headline forte, corpo persuasivo) e Título do Anúncio.
        - Se for TikTok: Foque em ganchos (hooks) rápidos para os primeiros 3 segundos de vídeo.
        - NÃO use aspas nas respostas.
        
        {regra_black}
        """
        
        prompt_usuario = f"""
        Crie uma estrutura completa de campanha para:
        Plataforma: {plataforma}
        Tipo de Nicho: {tipo_nicho}
        Produto: {nome_produto}
        URL: {url_site}
        Público: {publico_alvo}
        Benefícios: {beneficios}
        
        SAÍDA OBRIGATÓRIA NESTE FORMATO EXATO:
        
        =========================================
        📝 1. TEXTOS DO ANÚNCIO (COPY)
        =========================================
        (Se Google: 15 Títulos de 30 chars, 4 Descrições de 90 chars e 6 Sitelinks curtos)
        (Se Face/TikTok: Textos Principais/Ganchos e Títulos blindados)
        
        =========================================
        🎯 2. CONFIGURAÇÃO DA CAMPANHA (O SEGREDO)
        =========================================
        - Objetivo da Campanha Recomendado:
        - Palavras-chave ou Interesses: (10 termos fortes)
        - Dispositivos: 
        - Estratégia de Lance Recomendada: 
        - Extensões adicionais (Snippets, etc):
        
        =========================================
        👥 3. ANÁLISE DO PÚBLICO E ÂNGULO
        =========================================
        - Qual a principal dor desse público?
        - Qual a objeção que precisa ser quebrada na página de vendas?
        """

        with st.spinner(f"🤖 O Cérebro Tubarão está montando sua campanha Blindada de {plataforma}..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": prompt_sistema},
                        {"role": "user", "content": prompt_usuario}
                    ],
                    temperature=0.7
                )
                
                resultado = response.choices[0].message.content
                
                # Exibição Bonita
                st.success(f"✅ Campanha de {plataforma} ({tipo_nicho}) Gerada com Sucesso!")
                st.text_area("Copie sua Campanha e Estrutura Aqui:", value=resultado, height=600)
                
            except Exception as e:
                st.error(f"Erro ao conectar na IA: {e}")

# ================= RODAPÉ =================
st.markdown("---")
st.caption("Desenvolvido por Papai & Parceiro Ltda. 🦅")
