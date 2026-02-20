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
        nome_produto = st.text_input("Nome do Produto/Serviço", placeholder="Ex: Robô V21 Forex")
    with col3:
        url_site = st.text_input("Site (URL)", placeholder="Ex: www.robov21.com.br")
    
    col4, col5 = st.columns(2)
    with col4:
        publico_alvo = st.text_input("Público Alvo (Quem compra?)", placeholder="Ex: Investidores iniciantes que querem renda extra")
    with col5:
        beneficios = st.text_area("Principais Benefícios (Ouro)", placeholder="Ex: Automático, Risco Baixo, Instalação Fácil...", height=68)
    
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
        
        # O PROMPT DE ENGENHARIA (O Segredo do App - Agora com Tráfego Completo)
        prompt_sistema = """
        Você é um Especialista Sênior em Tráfego Pago e Copywriting (Nível Gestor Elite).
        Sua missão é criar a estrutura de textos de alta conversão E o passo a passo de configuração da campanha na plataforma escolhida, agindo como um professor de tráfego.
        
        REGRAS DE OURO PARA TEXTOS:
        - Se for Google Ads: Títulos MÁXIMO 30 CARACTERES. Descrições MÁXIMO 90 CARACTERES. Sitelinks Max 25 caracteres. (Conte cada letra e espaço. Se passar, você falha).
        - Se for Facebook/Insta: Crie a Copy Principal (Headline forte, corpo persuasivo) e Título do Anúncio.
        - Se for TikTok: Foque em ganchos (hooks) rápidos para os primeiros 3 segundos de vídeo.
        - Use Gatilhos Mentais: Urgência, Autoridade, Ganância.
        - NÃO use aspas nas respostas.
        """
        
        prompt_usuario = f"""
        Crie uma estrutura completa de campanha para:
        Plataforma: {plataforma}
        Produto: {nome_produto}
        URL: {url_site}
        Público: {publico_alvo}
        Benefícios: {beneficios}
        
        SAÍDA OBRIGATÓRIA NESTE FORMATO EXATO (Adapte os textos para a plataforma escolhida):
        
        =========================================
        📝 1. TEXTOS DO ANÚNCIO (COPY)
        =========================================
        (Aqui entram os 15 Títulos de 30 chars, 4 Descrições de 90 chars e Sitelinks para Google, OU os Textos Principais/Títulos para Face/TikTok)
        
        =========================================
        🎯 2. CONFIGURAÇÃO DA CAMPANHA (O SEGREDO)
        =========================================
        - Objetivo da Campanha Recomendado: (Ex: Vendas, Leads, Tráfego)
        - Palavras-chave ou Interesses: (Liste 10 termos fortes para segmentar)
        - Dispositivos: (Recomendação de focar só em Celular, PC, ou ambos, e por quê)
        - Estratégia de Lance Recomendada: (Ex: Maximizar Conversões, CPA Desejado)
        - Extensões adicionais (Snippets, Frases de destaque, etc.)
        
        =========================================
        👥 3. ANÁLISE DO PÚBLICO E ÂNGULO
        =========================================
        - Qual a principal dor desse público?
        - Qual a objeção que precisa ser quebrada na página de vendas?
        """

        with st.spinner(f"🤖 O Cérebro Tubarão está montando sua campanha de {plataforma}..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-4o-mini", # Modelo rápido e barato
                    messages=[
                        {"role": "system", "content": prompt_sistema},
                        {"role": "user", "content": prompt_usuario}
                    ],
                    temperature=0.7
                )
                
                resultado = response.choices[0].message.content
                
                # Exibição Bonita
                st.success(f"✅ Campanha de {plataforma} Gerada com Sucesso!")
                st.text_area("Copie sua Campanha e Estrutura Aqui:", value=resultado, height=600)
                
            except Exception as e:
                st.error(f"Erro ao conectar na IA: {e}")

# ================= RODAPÉ =================
st.markdown("---")
st.caption("Desenvolvido por Papai & Parceiro Ltda. 🦅")
