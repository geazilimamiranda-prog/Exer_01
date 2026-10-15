import streamlit as st

# Configuração inicial da página (Título e Ícone na aba do navegador)
st.set_page_config(
    page_title="Calculadora Vibe Coding",
    page_icon="🧮",
    layout="centered"
)

# 1. Título principal com ícone amigável
st.title("🧮 Minha Primeira Calculadora em Streamlit")
st.write("Um aplicativo simples e elegante desenvolvido com Python para iniciantes.")

# Divisor visual
st.markdown("---")

# Criando colunas para organizar os campos de entrada de forma elegante
col1, col2 = st.columns(2)

with col1:
    # 2. Primeiro campo de entrada numérica com valor padrão 0.0
    num1 = st.number_input("Digite o primeiro número:", value=0.0, format="%.2f")

with col2:
    # 2. Segundo campo de entrada numérica com valor padrão 0.0
    num2 = st.number_input("Digite o segundo número:", value=0.0, format="%.2f")

# 3. Componente de seleção para escolher a operação
operacao = st.selectbox(
    "Escolha a operação desejada:",
    ("Soma (+)", "Subtração (-)", "Multiplicação (*)", "Divisão (/)")
)

st.markdown("")

# 4. Botão de ação com o texto "Calcular"
if st.button("Calcular", type="primary", use_container_width=True):
    resultado = None
    erro = None
    
    # Lógica dos cálculos baseada na seleção
    if operacao == "Soma (+)":
        resultado = num1 + num2
    elif operacao == "Subtração (-)":
        resultado = num1 - num2
    elif operacao == "Multiplicação (*)":
        resultado = num1 * num2
    elif operacao == "Divisão (/)":
        # 5. Tratamento de divisão por zero
        if num2 == 0:
            erro = "⚠️ Erro: Não é possível realizar divisão por zero!"
        else:
            resultado = num1 / num2

    # 5. Exibição dos resultados ou mensagens de erro
    if erro:
        st.error(erro)
    else:
        st.markdown("---")
        st.success("Cálculo realizado com sucesso! 🎉")
        # Mostrando o resultado em grande destaque usando st.metric
        st.metric(label="Resultado Final", value=f"{resultado:.4f}".rstrip('0').rstrip('.'))

# Rodapé explicativo
st.markdown("---")
st.caption("Desenvolvido com ❤️ usando Python e Streamlit.")
