# -*- coding: utf-8 -*-
import streamlit as st
from openai import OpenAI

# ================= CONFIGURAÇÃO DA PÁGINA =================
st.set_page_config(page_title="Gestor Ads Pro Elite", page_icon="🚀", layout="wide")

st.title("🚀 Máquina de Campanhas e Tráfego Pago")
st.markdown("""
**Transforme seu produto em uma campanha pronta em segundos.**
*Copywriter + Gestor de Tráfego: Textos milimétricos e configurações exatas (Públicos, Dispositivos e Estratégia).*
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

            # REGRA ESPECÍFICA PARA FACEBOOK ADS COM A ESTRUTURA DO PAPAI
            estrutura_trafego = ""
            if "Facebook" in plataforma:
                estrutura_trafego = """
                =========================================
                2. PASSO A PASSO DA CAMPANHA (O MAPA DA MINA)
                =========================================
                (Entregue EXATAMENTE esta estrutura de configuracao para o cliente preencher no Facebook, adicionando dicas rapidas relacionadas ao produto dele):
                
                NIVEL 1: CAMPANHA
                - Tipo de Compra: Leilao
                - Objetivo da Campanha: Vendas
                - Orcamento de Campanha Advantage+ (CBO): Ativado
                - Estrategia de Orcamento: Volume mais alto
                - Orcamento Diario Sugerido: R$ 25,00 (Para teste inicial)
                
                NIVEL 2: CONJUNTO DE ANUNCIOS
                - Meta de Desempenho: Maximizar numero de conversoes
                - Pixel / Evento: Selecione seu Pixel -> Evento: Iniciar Finalizacao de Compra (Initiate Checkout)
                - Publico Advantage+: Ativado
                - Localizacao: Inclusao - Brasil
                - Segmentacao: (Sugira 1 ou 2 direcionamentos focados no publico-alvo, ex: excluir compradores dos ultimos 90 dias)
                - Posicionamentos: Advantage+ Ativado (Deixe a Meta escolher onde performa melhor)
                
                NIVEL 3: ANUNCIO
                - Nome do Anuncio: (Crie um nome baseado no angulo)
                - Formato: (Sugira imagem ou video)
                - Rastreamento: Eventos do Site ativados
                - Parametros de URL (UTM): (Crie um exemplo de UTM basico para este anuncio)
                """
            else:
                estrutura_trafego = """
                =========================================
                2. CONFIGURACAO DA CAMPANHA (O SEGREDO)
                =========================================
                - Objetivo da Campanha Recomendado:
                - Palavras-chave ou Interesses: (10 termos fortes)
                - Dispositivos: 
                - Estrategia de Lance Recomendada: 
                - Extensoes adicionais:
                """

            # O PROMPT DE ENGENHARIA 
            prompt_sistema = f"""
            Voce e um Especialista Senior em Trafego Pago e Copywriting.
            
            REGRAS DE OURO PARA TEXTOS:
            - Google Ads: Titulos MAX 30 CARACTERES. Descricoes MAX 90 CARACTERES. Sitelinks MAX 25.
            - Facebook/TikTok: Foque em ganchos e headlines blindadas.
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
            1. TEXTOS DO ANUNCIO (COPY)
            =========================================
            (Escreva a copy respeitando rigorosamente os limites de caracteres e as regras da plataforma)
            
            {estrutura_trafego}
            
            =========================================
            3. ANALISE DO PUBLICO E ANGULO
            =========================================
            - Qual a principal dor desse publico?
            - Qual a objecao que precisa ser quebrada na pagina de vendas?
            """

            with st.spinner("🤖 O Cérebro Tubarão está montando seu curso e campanha..."):
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": prompt_sistema},
                        {"role": "user", "content": prompt_usuario}
                    ],
                    temperature=0.7
                )
                
                resultado = response.choices[0].message.content
                
                st.success("✅ Guia de Tráfego e Copy Gerados com Sucesso!")
                st.text_area("Copie sua Estrutura Completa Aqui:", value=resultado, height=650)
                
        except Exception as e:
            st.error(f"Erro ao conectar na IA (Verifique sua chave): {e}")

# ================= RODAPÉ =================
st.markdown("---")
st.caption("Desenvolvido por Papai & Parceiro Ltda. 🦅")
