# -*- coding: utf-8 -*-
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
        
        # INSTRUÇÕES DE CONTINGÊNCIA (NICHO BLACK) - Sem Emojis para não dar erro de ASCII
        regra_black = ""
        if tipo_nicho == "Nicho Black (Risco de Bloqueio)":
            regra_black = """
            ALERTA DE NICHO BLACK (CONTINGENCIA ATIVADA):
            - O rigor com as politicas da plataforma e MAXIMO.
            - PROIBIDO usar palavras que dao ban/bloqueio (ex: "rapido", "garantido", "dinheiro facil", "cura", "perder peso", "fique rico").
            - Use COPY BLINDADA: Trabalhe com curiosidade, metaforas, e foque no "mecanismo unico" ao inves da promessa agressiva.
            - O texto precisa passar pela aprovacao automatica do robo da plataforma sem levantar suspeitas (zero claims exagerados).
            """
        else:
            regra_black = "- Nicho White: Foque nos beneficios diretos e transformacao clara, mantendo as boas praticas da plataforma."

        # O PROMPT DE ENGENHARIA (O Segredo do App)
        prompt_sistema = f"""
        Voce e um Especialista Senior em Trafego Pago e Copywriting (Nivel Gestor Elite).
        Sua missao e criar a estrutura de textos de alta conversao E o passo a passo de configuracao da campanha na plataforma escolhida.
        
        REGRAS DE OURO PARA TEXTOS:
        - Se for Google Ads: Titulos MAXIMO 30 CARACTERES. Descricoes MAXIMO 90 CARACTERES. Sitelinks Max 25 caracteres. (Conte cada letra e espaco. Se passar, voce falha).
        - Se for Facebook/Insta: Crie a Copy Principal (Headline forte, corpo persuasivo) e Titulo do Anuncio.
        - Se for TikTok: Foque em ganchos (hooks) rapidos para os primeiros 3 segundos de video.
        - NAO use aspas nas respostas.
        
        {regra_black}
        """
        
        prompt_usuario = f"""
        Crie uma estrutura completa de campanha para:
        Plataforma: {plataforma}
        Tipo de Nicho: {tipo_nicho}
        Produto: {nome_produto}
        URL: {url_site}
        Publico: {publico_alvo}
        Beneficios: {beneficios}
        
        SAIDA OBRIGATORIA NESTE FORMATO EXATO:
        
        =========================================
        1. TEXTOS DO ANUNCIO (COPY)
        =========================================
        (Se Google: 15 Titulos de 30 chars, 4 Descricoes de 90 chars e 6 Sitelinks curtos)
        (Se Face/TikTok: Textos Principais/Ganchos e Titulos blindados)
        
        =========================================
        2. CONFIGURACAO DA CAMPANHA (O SEGREDO)
        =========================================
        - Objetivo da Campanha Recomendado:
        - Palavras-chave ou Interesses: (10 termos fortes)
        - Dispositivos: 
        - Estrategia de Lance Recomendada: 
        - Extensoes adicionais (Snippets, etc):
        
        =========================================
        3. ANALISE DO PUBLICO E ANGULO
        =========================================
        - Qual a principal dor desse publico?
        - Qual a objecao que precisa ser quebrada na pagina de vendas?
        """

        with st.spinner(f"O Cerebro Tubarao esta montando sua campanha de {plataforma}..."):
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
