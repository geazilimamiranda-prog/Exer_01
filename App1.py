import streamlit as st

# Configuração inicial da página
st.set_page_config(
    page_title="Calculadora Vibe Coding",
    page_icon="🧮",
    layout="centered"
)

# Estilização CSS para os botões com relevo e para o balão de fala animado
st.markdown("""
    <style>
    /* Estilo com relevo e sombra para os botões */
    div.stButton > button {
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2), 0px 1px 3px rgba(0, 0, 0, 0.1);
        border-radius: 8px;
        transition: all 0.2s ease-in-out;
    }
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0px 6px 10px rgba(0, 0, 0, 0.25);
    }
    div.stButton > button:active {
        transform: translateY(1px);
        box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.15);
    }

    /* Estilo do balão de fala moderno */
    .speech-bubble {
        position: relative;
        background: #f0f8ff;
        border: 2px solid #0068c9;
        border-radius: 12px;
        padding: 15px 20px;
        margin-top: 10px;
        margin-bottom: 20px;
        box-shadow: 0px 4px 12px rgba(0, 104, 201, 0.15);
        animation: fadeIn 0.4s ease-in-out;
    }
    .speech-bubble:after {
        content: '';
        position: absolute;
        bottom: 100%;
        left: 30px;
        margin-left: -10px;
        border-width: 10px;
        border-style: solid;
        border-color: transparent transparent #0068c9 transparent;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-8px); }
        to { opacity: 1; transform: translateY(0); }
    }
    </style>
""", unsafe_allow_html=True)

# 1. Título principal com ícone amigável
st.title("🧮 Calculadora com Balão Interativo")
st.write("Selecione a operação, informe os números e acione o cálculo para ver a mágica acontecer.")

st.markdown("---")

# Inicializa o estado da sessão para guardar a operação selecionada
if "operacao_selecionada" not in st.session_state:
    st.session_state.operacao_selecionada = "Soma (+)"

# 2. Dois campos de entrada numérica
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("Digite o primeiro número:", value=0.0, format="%.2f")

with col2:
    num2 = st.number_input("Digite o segundo número:", value=0.0, format="%.2f")

st.markdown("### 1. Selecione a Operação:")

# Botões de seleção de operação em colunas
btn_col1, btn_col2, btn_col3, btn_col4 = st.columns(4)

with btn_col1:
    if st.button("➕ Soma", use_container_width=True):
        st.session_state.operacao_selecionada = "Soma (+)"

with btn_col2:
    if st.button("➖ Subtração", use_container_width=True):
        st.session_state.operacao_selecionada = "Subtração (-)"

with btn_col3:
    if st.button("✖️ Multiplicação", use_container_width=True):
        st.session_state.operacao_selecionada = "Multiplicação (*)"

with btn_col4:
    if st.button("➗ Divisão", use_container_width=True):
        st.session_state.operacao_selecionada = "Divisão (/)"

# Exibe qual operação está selecionada no momento
st.info(f"Operação selecionada: **{st.session_state.operacao_selecionada}**")

st.markdown("### 2. Clique para acionar o resultado:")

# 3, 4 & 5. Botão de ação com relevo para acionar e obter o resultado
if st.button("🚀 CALCULAR AGORA", type="primary", use_container_width=True):
    op = st.session_state.operacao_selecionada
    resultado = None
    erro = None
    
    if op == "Soma (+)":
        resultado = num1 + num2
    elif op == "Subtração (-)":
        resultado = num1 - num2
    elif op == "Multiplicação (*)":
        resultado = num1 * num2
    elif op == "Divisão (/)":
        if num2 == 0:
            erro = "⚠️ Erro: Não é possível realizar divisão por zero!"
        else:
            resultado = num1 / num2

    # Exibição do resultado ou do erro
    if erro:
        st.error(erro)
    else:
        st.success("Cálculo efetuado com sucesso! 🎉")
        
        # Formatando o valor e criando o balão de fala personalizado
        valor_formatado = f"{resultado:.4f}".rstrip('0').rstrip('.')
        
        st.markdown(f"""
            <div class="speech-bubble">
                <h4 style="margin: 0; color: #0068c9;">💬 Mensagem do Sistema:</h4>
                <p style="margin: 5px 0 0 0; font-size: 16px; color: #31333F;">
                    O resultado da operação <b>{op}</b> entre <b>{num1}</b> e <b>{num2}</b> é: <b style="color: #2b9348; font-size: 18px;">{valor_formatado}</b>
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        # Mostrando também a métrica tradicional em destaque
        st.metric(label=f"Resumo Final ({op})", value=valor_formatado)

st.markdown("---")
st.caption("Desenvolvido com ❤️ usando Python e Streamlit.")
