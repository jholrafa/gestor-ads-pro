import streamlit as st
from openai import OpenAI

# 1. CONFIGURAÇÃO DA PÁGINA (Deixa a tela larga e coloca o ícone da águia na aba do navegador)
st.set_page_config(page_title="Gestor Ads Elite", page_icon="🦅", layout="wide")

# 2. BARRA LATERAL (Área do Cliente e API)
with st.sidebar:
    st.title("🦅 Gestor Ads Elite")
    st.markdown("---")
    api_key = st.text_input("🔑 Sua Chave API (OpenAI):", type="password", help="Sua chave é segura e não é salva no nosso banco de dados.")
    
    if api_key:
        st.success("✅ Sistema Conectado e Pronto!")
    else:
        st.warning("⚠️ Insira sua chave para liberar o motor.")
        
    st.markdown("---")
    st.info("💡 Dica do Tubarão: Quanto mais detalhes você colocar no público-alvo, mais a Inteligência Artificial vai acertar na dor do cliente!")

# 3. CABEÇALHO PRINCIPAL
st.title("🚀 Painel de Criação de Campanhas")
st.markdown("Gere **anúncios de alta conversão** em segundos sem precisar de um copywriter.")
st.markdown("---")

# 4. DASHBOARD - COLUNAS LADO A LADO
col1, col2 = st.columns(2)

with col1:
    nicho = st.text_input("🎯 Produto ou Nicho", placeholder="Ex: Emagrecimento, Opções Binárias, Hamburgueria...")

with col2:
    publico = st.text_input("👥 Público-Alvo", placeholder="Ex: Homens 25-40 anos que querem renda extra...")

# 5. CONFIGURAÇÕES AVANÇADAS (Fica escondidinho para dar um ar profissional)
with st.expander("⚙️ Configurações Avançadas da Campanha"):
    col_adv1, col_adv2 = st.columns(2)
    with col_adv1:
        tom_voz = st.selectbox("Tom de Voz do Anúncio:", ["Persuasivo & Agressivo (Venda Direta)", "Educativo & Autoridade", "Urgência & Escassez", "Curiosidade Extrema"])
    with col_adv2:
        plataforma = st.selectbox("Foco da Plataforma:", ["Google Ads (Rede de Pesquisa)", "Meta Ads (Facebook/Instagram)", "TikTok Ads", "YouTube Ads"])

st.markdown("<br>", unsafe_allow_html=True) # Dá um espacinho

# 6. O BOTÃO DE AÇÃO PRINCIPAL
if st.button("⚡ GERAR ANÚNCIO BLINDADO", use_container_width=True, type="primary"):
    if not api_key:
        st.error("🛑 Alto lá! Cole sua Chave API na barra lateral esquerda primeiro.")
    elif not nicho or not publico:
        st.warning("⚠️ Preencha o Nicho e o Público para o robô trabalhar direito.")
    else:
        with st.spinner("🧠 O Cérebro do Tubarão está analisando o mercado e escrevendo sua copy..."):
            try:
                # Conecta na OpenAI
                client = OpenAI(api_key=api_key)
                
                # A INSTRUÇÃO SECRETA DO PAPAI (O PROMPT)
                prompt = f"""
                Atue como o melhor copywriter de tráfego pago do mundo.
                Crie um anúncio para a plataforma {plataforma}.
                Nicho/Produto: {nicho}.
                Público-alvo: {publico}.
                Tom de voz: {tom_voz}.
                
                Me entregue o resultado dividido em 3 partes:
                1. 3 Opções de Títulos Magnéticos.
                2. A Copy Principal (Corpo do texto).
                3. Uma sugestão de Imagem ou Vídeo para usar nesse anúncio.
                """
                
                # Chama o robô da OpenAI
                resposta = client.chat.completions.create(
                    model="gpt-3.5-turbo", # Pode mudar pra gpt-4 se quiser mais inteligência
                    messages=[{"role": "user", "content": prompt}]
                )
                
                texto_gerado = resposta.choices[0].message.content
                
                st.success("🎯 Campanha Gerada com Sucesso!")
                
                # 7. EXIBIÇÃO EM ABAS (Chique demais!)
                st.markdown("### 🏆 Resultado da Sua Campanha")
                st.info(texto_gerado)
                
                # 8. BOTÃO DE DOWNLOAD PARA O CLIENTE LEVAR O ARQUIVO
                st.download_button(
                    label="💾 Baixar Campanha em Texto",
                    data=texto_gerado,
                    file_name="campanha_blindada.txt",
                    mime="text/plain"
                )
                
            except Exception as e:
                st.error(f"❌ Deu algum erro de comunicação com a OpenAI. Verifique sua chave API. Detalhe técnico: {e}")
