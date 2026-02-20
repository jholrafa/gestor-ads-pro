# -*- coding: utf-8 -*-
import streamlit as st
from openai import OpenAI

# ================= CONFIGURAÇÃO DA PÁGINA =================
st.set_page_config(page_title="Gestor Ads Pro Elite", page_icon="🚀", layout="wide")

st.title("🚀 Máquina de Campanhas e Tráfego Pago")
st.markdown("""
**Transforme seu produto em uma campanha pronta em segundos.**
*Copywriter + Gestor de Tráfego: Textos milimétricos e configurações exatas (Google, Facebook ou TikTok).*
""")

# ================= BARRA LATERAL (CONFIGURAÇÃO) =================
with st.sidebar:
    st.header("🔑 Configuração")
    chave_crua = st.text_input("Cole sua API Key da OpenAI aqui:", type="password")
    
    # Limpa espaços invisíveis que causam erro na chave
    api_key = chave_crua.strip() if chave_crua else ""
    
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
        try:
            client = OpenAI(api_key=api_key)
            
            # INSTRUÇÕES DE CONTINGÊNCIA
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

            # === O CÉREBRO INTELIGENTE: SEPARA GOOGLE DE FACEBOOK ===
            regras_textos = ""
            estrutura_trafego = ""
            
            if "Google" in plataforma:
                regras_textos = """
                1. 15 Titulos (MAXIMO 30 CARACTERES cada).
                2. 4 Descricoes (MAXIMO 90 CARACTERES cada).
                3. 6 Sitelinks curtos (MAXIMO 25 CARACTERES cada).
                4. 4 Frases de Destaque / Snippets Estruturados.
                5. 
                """
                estrutura_trafego = """
                =========================================
                🎯 2. CONFIGURACAO DA CAMPANHA (O MAPA DA MINA - GOOGLE ADS)
                =========================================
                - Objetivo da Campanha: (Ex: Vendas, Leads)
                - Palavras-chave Positivas: (10 termos quentes para comprar)
                - Palavras-chave Negativas: (10 termos cruciais para negativar e nao perder dinheiro)
                - Publico-Alvo Demografico: (Qual a Renda, Idade e Genero ideal?)
                - Dispositivos: (Focar em Celular, Computador ou ambos?)
                - Estrategia de Lance Recomendada: (Ex: Maximizar Conversoes)
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
                - Pixel / Evento: Selecionar o Pixel -> Evento: Iniciar Finalizacao de Compra (Initiate Checkout)
                - Publico Advantage+: Ativado
                - Localizacao: Inclusao - Brasil
                - Segmentacao: (Sugira interesses e exclusoes, ex: excluir compradores 90 dias)
                - Posicionamentos: Advantage+ Ativado
                
                NIVEL 3: ANUNCIO
                - Nome do Anuncio: (Crie um nome focado no angulo)
                - Rastreamento: Eventos do Site Ativados
                - Parametros de URL (UTM): (Crie o link com utm_source e utm_medium)
                """
                
            else: # TikTok
                regras_textos = "Ganchos (Hooks) para os 3 primeiros segundos de video e Texto curto para a legenda."
                estrutura_trafego = "Objetivo, Interesses e Comportamentos ideais no TikTok Ads."

            # O PROMPT DE ENGENHARIA 
            prompt_sistema = f"""
            Voce e um Especialista Senior em Trafego Pago e Copywriting.
            Sua missao e preencher as configuracoes tecnicas e escrever copys matadoras.
            
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
                
                # Exibição Bonita
                st.success(f"✅ Guia Completo para {plataforma} Gerado com Sucesso!")
                st.text_area("Copie sua Estrutura Completa Aqui:", value=resultado, height=650)
                
        except Exception as e:
            st.error(f"Erro ao conectar na IA (Verifique sua chave): {e}")

# ================= RODAPÉ =================
st.markdown("---")
st.caption("Desenvolvido por Papai & Parceiro Ltda. 🦅")
