import streamlit as st

# Configuração inicial da página
st.set_page_config(
    page_title="Calculadora Vibe Coding",
    page_icon="🧮",
    layout="centered"
)

# Estilização CSS personalizada para dar efeito de RELEVO nos botões
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
    </style>
""", unsafe_allow_html=True)

# 1. Título principal com ícone amigável
st.title("🧮 Calculadora com Botões de Relevo")
st.write("Selecione a operação, insira os números e acione o botão para obter o resultado.")

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

# 3, 4 & 5. Botão de ação com RELEVO para acionar e obter o resultado
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
        valor_formatado = f"{resultado:.4f}".rstrip('0').rstrip('.')
        st.metric(label=f"Resultado ({op})", value=valor_formatado)

st.markdown("---")
st.caption("Desenvolvido com ❤️ usando Python e Streamlit.")
